import requests
from io import BytesIO
import librosa
from ..utils import timer
import numpy as np
from typing import Dict, List, Tuple
import traceback
from loguru import logger
import re
import json
from pathlib import Path
from funasr.utils.load_utils import load_audio_text_image_video
import threading


BEST_BATCH_SIZE_S_FILE = (
    Path(__file__).parent.parent / "asset" / "best_batch_size_s.json"
)


class ASRInference:
    """ASR wpai 服务推理基类,一般情况下只需要实现inference和setup方法"""

    def __init__(
        self,
        # 模型路径
        model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        vad_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        punc_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        # 组批次推理
        batch_size_s: int = 30,
        batch_size: int = 10,
        batch_size_threshold_s: int = 60,
        # 输入音频相关
        max_duration_seconds: int = 7200,
        sample_rate: int = 16000,
        librosa_resample: bool = True,
        # onnx推理
        quantize: bool = False,
        use_cpu: bool = False,
        num_threads: int = 4,
        # 动态batch_size_s
        dynamic_batch_size_s: bool = True,
        # 返回格式
        return_json: bool = True,
        # 其他参数
        lock_thread: bool = True,
    ):
        """
        Args:
            model_dir (str, optional): asr模型目录. Defaults to "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch".
            vad_dir (str, optional): vad模型目录. Defaults to "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch".
            punc_dir (str, optional): 标点符号模型目录. Defaults to "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch".

            batch_size_s (int, optional): asr模型批次推理总时长. Defaults to 30s.
            batch_size (int, optional): asr模型批次推理. Defaults to 10.
            batch_size_threshold_s (int, optional): asr模型批次推理单个音频的最大时长. Defaults to 60s.

            max_duration_seconds (int, optional): 音频文件最大时长. Defaults to 7200.
            sample_rate (int, optional): 音频文件采样率. Defaults to 16000.
            librosa_resample (bool, optional): 是否使用librosa重采样. Defaults to false.

            quantize (bool, optional): onnx模型是否量化. Defaults to False.
            use_cpu (bool, optional): 是否使用cpu推理. Defaults to False.
            num_threads (int, optional): onnx模型cpu推理时候的线程数. Defaults to 4.

            dynamic_batch_size_s (bool, optional): 是否动态选择batch_size_s. Defaults to False.

            return_json (bool, optional): 是否返回json格式. Defaults to True.
            lock_thread (bool, optional): 是否锁定线程. Defaults to True.
        """
        super().__init__()

        self.model_dir = model_dir
        self.vad_dir = vad_dir
        self.punc_dir = punc_dir

        self.batch_size_s = batch_size_s
        self.batch_size_threshold_s = batch_size_threshold_s
        with open(BEST_BATCH_SIZE_S_FILE, "r") as f:
            self.best_batch_size_s_file = json.load(f)
        self.dynamic_batch_size_s = dynamic_batch_size_s
        self.max_duration_seconds = max_duration_seconds
        self.sample_rate = sample_rate
        self.librosa_resample = librosa_resample
        self.batch_size = batch_size

        self.quantize = quantize
        self.device_id = -1 if use_cpu else 0
        self.num_threads = num_threads

        self.return_json = return_json

        self.lock_thread = lock_thread
        if self.lock_thread:
            self.lock = threading.Lock() # 用于多线程推理时候的锁

        self.setup()

    @timer("load audio")
    def load_audio_bytes(self, bytes, sr: int) -> Tuple[np.ndarray, float, int]:
        """加载音频文件

        Args:
            bytes (_type_): 音频文件字节流
            sr (int): 音频采样率

        Returns:
            Tuple[np.ndarray, float, int]: 音频数据，音频时长，音频采样率
        """
        file = BytesIO(bytes)
        if self.librosa_resample:
            audio, sr = librosa.load(file, mono=False, sr=sr)
        else:
            audio, sr = librosa.load(
                file, mono=False, sr=None
            )  # sr=none为原始音频采样率
        duration = librosa.get_duration(y=audio, sr=sr)
        return audio, duration, sr

    @timer("upsample audio")
    def upsample_audio(self, audio: np.ndarray, sr: int) -> np.ndarray:
        """重采样音频

        Args:
            audio (np.ndarray): 音频数据
            sr (int): 原始音频采样率

        Returns:
            np.ndarray: 重采样后的音频数据
        """
        audio = load_audio_text_image_video(
            audio, fs=self.sample_rate, audio_fs=sr
        )  # 使用官方方式重采样
        return audio

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
                else:
                    logger.info(f"audio duration seconds {ds}")
                    if ds < 0.5:
                        res["data"] = ""
                        res["code"] = 0
                        res["msg"] = f"输入的音频太短了{ds}s，不解析"
                    elif (
                        ds >= self.max_duration_seconds
                    ):  # 超过2个小时的超长音频，这里不做解析。
                        res["data"] = ""
                        res["code"] = 0
                        res["msg"] = "音频时长超过2小时，不解析"
                    else:
                        if self.dynamic_batch_size_s:
                            self.batch_size_s = self.get_best_batch_size_s(ds)
                            logger.info(f"dynamic batch_size_s: {self.batch_size_s}")
                        if sr != self.sample_rate:
                            audio = self.upsample_audio(audio, sr)
                        d_left, d_right = self.inference([audio[0], audio[1]])

                        data = self.post_process(d_left, d_right)

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

    @timer("post process")
    def post_process(self, d_left, d_right) -> Dict[str, str]:
        data = dict()
        sentence_all = []
        text_all = dict()
        text_all["left"] = ""
        text_all["right"] = ""

        if "text" in d_left:
            text_all["left"] = d_left["text"].replace(" ", "")
        if "sentence_info" in d_left:
            for s in d_left["sentence_info"]:
                s["text"] = re.sub(r"[^\w\s]", "", s["text"])
                s["startTime"] = s["timestamp"][0][0]
                s["endTime"] = s["timestamp"][-1][1]
                s["duration"] = s["endTime"] - s["startTime"]
                s["channel"] = "left"
                del s["start"]
                del s["end"]
                del s["timestamp"]
            sentence_all += d_left["sentence_info"]

        if "text" in d_right:
            text_all["right"] = d_right["text"].replace(" ", "")
        if "sentence_info" in d_right:
            for s in d_right["sentence_info"]:
                s["text"] = re.sub(r"[^\w\s]", "", s["text"])
                s["startTime"] = s["timestamp"][0][0]
                s["endTime"] = s["timestamp"][-1][1]
                s["duration"] = s["endTime"] - s["startTime"]
                s["channel"] = "right"
                del s["start"]
                del s["end"]
                del s["timestamp"]
            sentence_all += d_right["sentence_info"]

        sentence_all.sort(key=lambda x: x["startTime"])
        for idx, _ in enumerate(sentence_all):
            sentence_all[idx]["sentenceIndex"] = idx

        data["text"] = text_all
        data["sentences"] = sentence_all
        return data

    @timer("search best batch_size_s", round_num=4)
    def get_best_batch_size_s(self, duration_seconds: float) -> int:
        """根据音频时长获取最适合的batch_size_s
        To do: 优化算法，目前是遍历，可以优化为二分查找
        """
        for i, d in enumerate(self.best_batch_size_s_file):
            if d["duration"] >= duration_seconds:
                # 判断跟当前的duration_seconds最接近的一个
                if i == 0:
                    return int(d["batch_size_s"])
                else:
                    if (
                        duration_seconds
                        - self.best_batch_size_s_file[i - 1]["duration"]
                        > d["duration"] - duration_seconds
                    ):
                        return int(d["batch_size_s"])
                    else:
                        return int(self.best_batch_size_s_file[i - 1]["batch_size_s"])
        return int(self.best_batch_size_s_file[-1]["batch_size_s"])

    def inference(self, audios: List[np.ndarray]):
        raise NotImplementedError()

    def setup(self) -> None:
        raise NotImplementedError()

    def eval(self, *args, **kwargs) -> None:
        """wpai 平台接口，必须实现,不然报错"""
        pass

    def to(self, *args, **kwargs) -> None:
        """wpai 平台接口，必须实现,不然报错"""
        pass
