from jsonargparse import CLI
from .inferences import OnnxInference, TorchInference
from .utils import prepare_models, download
from .tests.latency import compare_latency
from .tests.utils import get_grpc_result
from pathlib import Path
from typing import Literal, Optional


BADE_CASE_DIR = Path(__file__).parent / "asset" / "badcase.txt"
AUDIO_URL_FILE = Path(__file__).parent.parent / "asset" / "audio_urls.txt"


class Test:
    """测试pytorch和onnx runtime推理速度"""

    def __init__(
        self,
        model_dir: str = "checkpoints/iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
        punc_dir: str = "checkpoints/iic/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
        vad_dir: str = "checkpoints/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
        batch_size_s: int = 30,
        batch_size: int = 10,
        batch_size_threshold_s: int = 60,
        max_duration_seconds: int = 7200,
        sample_rate: int = 16000,
        n: int = 10,
    ):
        super().__init__()

        self.model_dir = model_dir
        self.punc_dir = punc_dir
        self.vad_dir = vad_dir
        self.batch_size_s = batch_size_s
        self.batch_size = batch_size
        self.batch_size_threshold_s = batch_size_threshold_s
        self.max_duration_seconds = max_duration_seconds
        self.sample_rate = sample_rate
        self.n = n

    def pytorch(self, url: str):
        """测试pytorch推理速度

        Args:
            url (str): 音频数据地址
        """
        infer = TorchInference(
            model_dir=self.model_dir,
            punc_dir=self.punc_dir,
            vad_dir=self.vad_dir,
            batch_size_s=self.batch_size_s,
            batch_size=self.batch_size,
            batch_size_threshold_s=self.batch_size_threshold_s,
        )
        for i in range(self.n):
            result = infer.predict(url)

    def badcase(self):
        """测试badcase"""
        infer = TorchInference(
            model_dir=self.model_dir,
            punc_dir=self.punc_dir,
            vad_dir=self.vad_dir,
            batch_size_s=self.batch_size_s,
            batch_size=self.batch_size,
            batch_size_threshold_s=self.batch_size_threshold_s,
        )
        with open(BADE_CASE_DIR, "r") as f:
            for line in f:
                url = line.strip()
                result = infer.predict(url)

    def onnx(
        self,
        url: str,
        quantize: bool = False,
        use_cpu: bool = False,
        num_threads: int = 4,
    ):
        """测试onnx runtime推理速度

        Args:
            url (str): 音频地址
            quantize (bool, optional): 是否使用量化模型. Defaults to False.
            use_cpu (bool, optional): 是否使用cpu. Defaults to False.
            num_threads (int, optional): 使用cpu推理的物理核数量. Defaults to 4.
        """
        infer = OnnxInference(
            model_dir=self.model_dir,
            punc_dir=self.punc_dir,
            quantize=quantize,
            use_cpu=use_cpu,
            num_threads=num_threads,
        )
        for i in range(self.n):
            result = infer.predict(url)

    def service(
            self,
            task_id: str,
            url: Optional[str] = None,
            business: str = "huangye",
            env: Literal['test', 'ol'] = 'test',
    ):
        """测试grpc服务

        Args:
            url (str): 音频地址,或者文件，文件中每行为音频地址。
            task_id (str): 任务id
            business (str, optional): 业务类型. Defaults to "huangye".
            env (Literal['test', 'ol'], optional): 环境. Defaults to 'test'.
        """
        if not url:
            # 测试badcase
            with open(BADE_CASE_DIR, "r") as f:
                for line in f:
                    url = line.strip()
                    result, spent_time = get_grpc_result(url=url, task_id=task_id, business=business, env=env, return_spent_time=True)
        if Path(url).is_file():
            with open(url, "r") as f:
                for line in f:
                    url = line.strip()
                    result, spent_time = get_grpc_result(url=url, task_id=task_id, business=business, env=env, return_spent_time=True)
        else:
            res, spent_time = get_grpc_result(url=url, task_id=task_id, business=business, env=env, return_spent_time=True)
        


commands = {
    "test": Test,
    "prepare": prepare_models,
    "download": download,
    "compare": compare_latency,
}


def run():
    CLI(commands)


if __name__ == "__main__":
    run()
