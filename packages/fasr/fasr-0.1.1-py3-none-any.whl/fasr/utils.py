import time
from typing import Callable, Tuple
from loguru import logger
import requests
import librosa
from io import BytesIO


def timer(tag: str, round_num: int = 2):
    def outter(func: Callable):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            res = func(*args, **kwargs)
            end = time.perf_counter()
            spent = round(end - start, round_num)
            logger.info(f"{tag} run in {spent} seconds")
            return res

        return wrapper

    return outter


def prepare_models(cache_dir: str = "checkpoints"):
    """Prepare models for funasr"""
    from modelscope import snapshot_download

    models = [
        "iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        "iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        "iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    ]
    for model in models:
        snapshot_download(model_id=model, cache_dir=cache_dir)


def download(model: str, revision: str = None, cache_dir: str = "checkpoints"):
    """Download model from modelscope"""
    from modelscope import snapshot_download

    model = snapshot_download(model, cache_dir=cache_dir, revision=revision)


def load_audio(url: str, sr: int = 16000, mono: bool = False) -> Tuple:
    """Load audio from url"""
    audio = requests.get(url).content
    audio = BytesIO(audio)
    audio, sr = librosa.load(audio, sr=sr, mono=mono)
    duration = librosa.get_duration(y=audio, sr=sr)
    return audio, duration
