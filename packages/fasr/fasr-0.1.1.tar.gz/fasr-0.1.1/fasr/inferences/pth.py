from funasr import AutoModel
from ..utils import timer, load_audio
from .base import ASRInference
from typing import List, Dict
import numpy as np
from loguru import logger
import requests
import json
import traceback
import torch


class TorchInference(ASRInference):
    @timer("load models")
    def setup(self) -> None:
        self.model = AutoModel(
            model=self.model_dir,
            sentence_timestamp=True,
            return_raw_text=False,
        )
        self.model.kwargs["batch_size"] = self.batch_size
        self.punc_model = AutoModel(
            model=self.punc_dir,
        )
        self.vad_model = AutoModel(
            model=self.vad_dir,
        )

    @timer("inference")
    def inference(self, audios: Dict):
        """输入是vad模型后的音频片段，将这些音频片段组成批次进行推理

        Args:
            audios (Dict): vad模型后的音频片段, {"对应key": {"audio": np.ndarray, "segments": [{"timestamp": [start, end]}]}}
        """
        # 1. 首先将所有音频的音频片段组合成一个列表，需要记录每个音频片段对应的音频key和它的音频片段的索引，以便后续整合为句子
        all_audio_segments = []
        for key in audios:
            audio_segments = audios[key]["segments"]
            for idx, segment in enumerate(audio_segments):
                segment["text"] = ""
                start = int(segment["timestamp"][0] * (self.sample_rate / 1000))
                end = int(segment["timestamp"][1] * (self.sample_rate / 1000))
                all_audio_segments.append(
                    {
                        "key": key,
                        "idx": idx,
                        "timestamp": segment["timestamp"],
                        "audio_slice": audios[key]["audio"][start:end],
                    }
                )

        # 2. 将音频片段根据持续时间排序，持续时间短的在前面
        sorted_segments = sorted(
            all_audio_segments, key=lambda x: x["timestamp"][1] - x["timestamp"][0]
        )

        # 3. 将音频片段组成批次，主要受到两个参数的影响，batch_size_s为每个批次的音频片段的总持续时间，batch_size_threshold_s为批次中的音频片段的最大持续时间
        beg_idx = 0
        end_idx = 1
        max_len_in_batch = 0
        batch_size = self.batch_size_s * 1000
        self.model.kwargs["batch_size"] = (
            batch_size  # 根据batch_size_s组成批次后，不需要在控制batch size
        )
        batch_size_threshold_ms = self.batch_size_threshold_s * 1000
        n = len(sorted_segments)
        for j, seg in enumerate(sorted_segments):
            sample_length = seg["timestamp"][1] - seg["timestamp"][0]
            potential_batch_length = max(max_len_in_batch, sample_length) * (
                j + 1 - beg_idx
            )
            if (
                j < n - 1
                and sample_length < batch_size_threshold_ms
                and potential_batch_length < batch_size
            ):
                max_len_in_batch = max(max_len_in_batch, sample_length)
                end_idx += 1
                continue
            results = self.model.generate(
                input=[seg["audio_slice"] for seg in sorted_segments[beg_idx:end_idx]]
            )
            for i, result in enumerate(results):
                sorted_segments[beg_idx + i]["text"] = result["text"]
                sorted_segments[beg_idx + i]["token_timestamp"] = result["timestamp"]
            beg_idx = end_idx
            end_idx += 1
            max_len_in_batch = sample_length

        # 4. 此时所有音频片段都已经识别完毕，将结果添加到原始音频信息中，并调用标点模型添加标点
        for seg in sorted_segments:
            audios[seg["key"]]["segments"][seg["idx"]]["text"] = seg["text"]
            audios[seg["key"]]["segments"][seg["idx"]]["token_timestamp"] = seg[
                "token_timestamp"
            ]
        for key in audios:
            tokens = []
            token_timestamp = []
            for seg in audios[key]["segments"]:
                tokens.append(seg["text"])
                start_seg = seg["timestamp"][0]
                for timestamp in seg["token_timestamp"]:
                    token_timestamp.append(
                        [start_seg + timestamp[0], start_seg + timestamp[1]]
                    )

            audios[key]["tokens"] = [t for token in tokens for t in token.split(" ")]
            audios[key]["token_timestamp"] = token_timestamp
            text = "".join(tokens).replace(" ", "")
            if len(text) > 0:
                punc_result = self.punc_model.generate(text)[0]
                audios[key]["text"] = punc_result["text"]
                audios[key]["punc_array"] = punc_result["punc_array"]
            else:
                audios[key]["text"] = ""
                audios[key]["punc_array"] = torch.empty(0)
        return audios

    @timer("predict")
    def predict(self, url: str, **kwargs) -> Dict[str, str]:
        if self.lock_thread:
            self.lock.acquire()
        res = {}
        try:
            logger.info(f"audio url: {url}")
            response = requests.get(url=url)
            if response.status_code == 200:
                audio, ds, sr = self.load_audio_bytes(
                    response.content, sr=self.sample_rate
                )
                channals = audio.shape[0]
                if channals != 2 or len(audio.shape) != 2:
                    res["data"] = ""
                    res["code"] = 0
                    res["msg"] = "输入的音频是单声道，不解析"
                    logger.warning(f"输入的音频声道异常，不是双声道音频，{channals}，不解析")
                else:
                    logger.info(f"audio duration seconds {ds}")
                    if ds < 0.5:
                        res["data"] = ""
                        res["code"] = 0
                        res["msg"] = f"输入的音频太短了{ds}s，不解析"
                        logger.warning(f"当前音频时长{ds}太短了，不解析")
                    elif (
                        ds >= self.max_duration_seconds
                    ):  # 超过2个小时的超长音频，这里不做解析。
                        res["data"] = ""
                        res["code"] = 0
                        res["msg"] = "音频时长超过2小时，不解析"
                        logger.warning(f"当前音频时长{ds}超过2小时，不解析")
                    else:
                        if self.dynamic_batch_size_s:
                            self.batch_size_s = self.get_best_batch_size_s(ds)
                            logger.info(f"dynamic batch_size_s: {self.batch_size_s}")
                        if sr != self.sample_rate:
                            audio = self.upsample_audio(audio, sr)
                        audios = self.split_audio(audio)
                        audios = self.inference(audios=audios)
                        data = self.post_process(audios=audios)

                        res["data"] = data
                        res["code"] = 0
                        res["msg"] = "success"
            else:
                res["code"] = -1
                res["msg"] = "download failure" + str(response)
                res["data"] = ""

        except Exception as e:
            errorMsg = "traceback.format_exc():\n%s" % traceback.format_exc()
            logger.error(errorMsg)
            logger.error(e.args)
            logger.error("url:{}".format(url))
            res["code"] = -1
            res["data"] = ""
            res["msg"] = "程序异常请联系管理员！" + errorMsg
        finally:
            if self.lock_thread:
                self.lock.release()

        if self.return_json:
            return json.dumps(res, ensure_ascii=False)
        return res

    def load_and_split(self, url: str):
        """获取测试音频的音频片段"""
        audio, duration = load_audio(url)
        left, right = np.split(audio, 2)
        left = left.squeeze()
        right = right.squeeze()
        audios = {}
        left_segments = self.vad_model.generate(left)[0]
        audios["left"] = {
            "audio": left,
            "segments": [{"timestamp": v, "text": ""} for v in left_segments["value"]],
        }
        right_segments = self.vad_model.generate(right)[0]
        audios["right"] = {
            "audio": right,
            "segments": [{"timestamp": v, "text": ""} for v in right_segments["value"]],
        }
        return audios

    @timer("split audio")
    def split_audio(self, audio: np.ndarray):
        """将音频分割成音频片段"""
        left, right = np.split(audio, 2)
        left = left.squeeze()
        right = right.squeeze()
        audios = {}
        left_segments = self.vad_model.generate(left)[0]
        audios["left"] = {
            "audio": left,
            "segments": [{"timestamp": v, "text": ""} for v in left_segments["value"]],
        }
        right_segments = self.vad_model.generate(right)[0]
        audios["right"] = {
            "audio": right,
            "segments": [{"timestamp": v, "text": ""} for v in right_segments["value"]],
        }
        return audios

    @timer("post process", round_num=3)
    def post_process(self, audios: Dict) -> Dict[str, str]:
        data = {"text": {"left": "", "right": ""}, "sentences": []}
        assert len(audios) == 2
        keys = list(audios.keys())
        all_sentences = []
        for i in range(2):
            key = keys[i]
            if i == 0:
                d_left = audios[key]
                if "text" in d_left:
                    data["text"]["left"] = d_left["text"].replace(" ", "")
                left_sentences = self.get_sentence_info(
                    punc_array=d_left["punc_array"],
                    asr_text=d_left["text"],
                    time_stamps=d_left["token_timestamp"],
                    channel="left",
                )
                all_sentences.extend(left_sentences)

            else:
                d_right = audios[key]
                if "text" in d_right:
                    data["text"]["right"] = d_right["text"].replace(" ", "")
                right_sentences = self.get_sentence_info(
                    punc_array=d_right["punc_array"],
                    asr_text=d_right["text"],
                    time_stamps=d_right["token_timestamp"],
                    channel="right",
                )
                all_sentences.extend(right_sentences)

        all_sentences.sort(key=lambda x: x["startTime"])
        for idx, _ in enumerate(all_sentences):
            all_sentences[idx]["sentenceIndex"] = idx
        data["sentences"] = all_sentences
        return data

    def get_sentence_info(
        self,
        punc_array: torch.Tensor,
        asr_text: str,
        time_stamps: List[List[int]],
        channel: str,
    ) -> Dict:
        """整合asr模型输出的结果和标点模型输出的结果，生成句子信息"""
        punc_ids = []
        punc_result_ids = punc_array.tolist()
        for idx, r in enumerate(punc_result_ids):
            if r != 1:
                punc_ids.append(idx)
        sentence_infos = []
        pre = 0
        for i, id in enumerate(punc_ids):
            sentence_info = {
                "text": "",
                "startTime": "",
                "endTime": "",
                "duration": "",
                "channel": channel,
            }
            if i == 0:
                text = asr_text[: id + 2]
                timestamp = time_stamps[: id + 1]
            else:
                pre = punc_ids[i - 1]
                text = asr_text[pre + 1 + i : id + 2 + i]
                timestamp = time_stamps[pre + 1 : id + 1]
            sentence_info["text"] = text
            sentence_info["startTime"] = timestamp[0][0]
            sentence_info["endTime"] = timestamp[-1][-1]
            sentence_info["duration"] = timestamp[-1][-1] - timestamp[0][0]
            sentence_infos.append(sentence_info)
        return sentence_infos


class TorchInferenceBaseline(ASRInference):
    """基于funasr的自动语音识别"""

    @timer("load models")
    def setup(self) -> None:
        self.model = AutoModel(
            vad_model=self.vad_dir,
            model=self.model_dir,
            punc_model=self.punc_dir,
            sentence_timestamp=True,
        )

    @timer("inference")
    def inference(self, audios: List[np.ndarray]):
        asr_results = []
        for audio in audios:
            asr_result = self.model.generate(audio, batch_size_s=self.batch_size_s)[0]
            asr_results.append(asr_result)
        return asr_results
