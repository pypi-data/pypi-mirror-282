from .utils import get_grpc_result
from typing import Dict, Optional
import librosa
import requests
from io import BytesIO
from tqdm import tqdm
from pathlib import Path
from random import choices
import time


AUDIO_URL_FILE = Path(__file__).parent.parent / "asset" / "audio_urls.txt"


def compare_latency(
    base_task_id: str,
    compare_task_id: str,
    compare_adjust: int = 1,
    file_path: Optional[str] = None,
    n: int = 300,
    business: str = "huangye",
    save_dir: str = "results",
    print_info: bool = False,
) -> Dict:
    """对比两个服务测试环境的延迟

    Args:
        base_task_id (str): 基准服务的task_id
        compare_task_id (str): 对比服务的task_id
        compare_adjust (int): 对比服务的延迟调整系数
        file_path (str): 音频url列表文件路径,如果为None则使用默认文件
        n (int): 测试音频数量
        business (str): 业务名称
        save_dir (str): 结果保存路径
        print_info (bool): 是否打印详细信息

    Returns:
        Dict: 返回两个服务的延迟对比结果
    """
    if not file_path:
        file_path = AUDIO_URL_FILE
    with open(file_path, "r") as f:
        lines = f.readlines()
    if len(lines) > n:
        lines = choices(lines, k=n)
    result = []
    for line in tqdm(lines):
        url = line.strip()
        try:
            duration, sr = get_audio_info(url)
            res_a, time_a = get_grpc_result(
                url,
                base_task_id,
                business,
                return_spent_time=True,
                print_info=print_info,
            )
            res_b, time_b = get_grpc_result(
                url,
                compare_task_id,
                business,
                return_spent_time=True,
                print_info=print_info,
            )
            result.append(
                {
                    "url": url,
                    "duration": duration,
                    "sample_rate": sr,
                    "base_time": time_a,
                    "base_result": res_a,
                    "compare_time": time_b,
                    "compare_result": res_b,
                    # 增长比例
                    "ratio": round((time_a - time_b) / time_a / compare_adjust, 2),
                }
            )
        except Exception as e:
            print(f"Error: {e}")
    # 根据测试时间保存结果
    save_dir = Path(
        save_dir, f"{base_task_id}_vs_{compare_task_id}", time.strftime("%Y%m%d%H%M%S")
    )
    if not save_dir.exists():
        save_dir.mkdir(parents=True)
    # 绘制对比图, y轴为延迟时间，x轴为音频时长, 并保存到save_dir命名为compare_latency.png
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.scatter(
        [item["duration"] for item in result],
        [item["base_time"] for item in result],
        label=f"service {base_task_id}",
    )
    plt.scatter(
        [item["duration"] for item in result],
        [item["compare_time"] for item in result],
        label=f"service {compare_task_id}",
    )
    plt.xlabel("audio duration(s)")
    plt.ylabel("latency(s)")
    plt.legend()
    plt.savefig(f"{save_dir}/compare.png")

    # 绘制增常比例图, y轴为增长比例，x轴为音频时长, 并保存到save_dir命名为compare_ratio.png
    plt.figure(figsize=(10, 6))
    plt.scatter(
        [item["duration"] for item in result], [item["ratio"] for item in result]
    )
    plt.xlabel("audio duration")
    plt.ylabel("ratio")
    plt.savefig(f"{save_dir}/compare_ratio.png")
    if len(result) > 0:
        base_runtime = sum([item["base_time"] for item in result]) / len(result)
        compare_runtime = sum([item["compare_time"] for item in result]) / len(result)
        final_result = {
            "base_task_id": base_task_id,
            "compare_task_id": compare_task_id,
            "base_runtime": round(base_runtime, 2),
            "compare_runtime": round(compare_runtime, 2),
            "runtime_diff": round(base_runtime - compare_runtime, 2),
            "runtime_diff_ratio": round(
                (base_runtime - compare_runtime) / base_runtime, 2
            ),
            "compare_adjust": compare_adjust,
            "mean_duration": round(
                sum([item["duration"] for item in result]) / len(result), 2
            ),
            "max_duration": max([item["duration"] for item in result]),
            "min_duration": min([item["duration"] for item in result]),
            "mean_ratio": round(
                sum([item["ratio"] for item in result]) / len(result), 2
            ),
            "max_ratio": max([item["ratio"] for item in result]),
            "min_ratio": min([item["ratio"] for item in result]),
            "result": result,
        }
        # 保存结果到save_dir命名为compare_result.json
        import json

        with open(f"{save_dir}/compare_result.json", "w", encoding="utf-8") as f:
            json.dump(final_result, f, indent=4, ensure_ascii=False)
        return final_result


def plot_latency(result: Dict, save_dir: str = "assets/compare_latency"):
    """绘制延迟对比结果图

    Args:
        result (Dict): compare_latency的返回结果
        save_dir (str): 保存路径
    """
    save_dir = Path(save_dir)
    if not save_dir.exists():
        save_dir.mkdir(parents=True)
    # 绘制对比图, y轴为延迟时间，x轴为音频时长, 并保存到save_dir命名为compare_latency.png
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.scatter(
        [item["duration"] for item in result["result"]],
        [item["base_time"] for item in result["result"]],
        label=f"service {result['base_task_id']}",
    )
    plt.scatter(
        [item["duration"] for item in result["result"]],
        [item["compare_time"] for item in result["result"]],
        label=f"service {result['compare_task_id']}",
    )
    plt.xlabel("audio duration(s)")
    plt.ylabel("latency(s)")
    plt.legend()
    plt.savefig(f"{save_dir}/compare.png")


def plot_ratio(result: Dict, save_dir: str = "assets/compare_latency"):
    """绘制延迟比例对比结果图

    Args:
        result (Dict): compare_latency的返回结果
        save_dir (str): 保存路径
    """
    import matplotlib.pyplot as plt

    save_dir = Path(save_dir)
    if not save_dir.exists():
        save_dir.mkdir(parents=True)
    # 绘制增常比例图, y轴为增长比例，x轴为音频时长, 并保存到save_dir命名为compare_ratio.png
    plt.figure(figsize=(10, 6))
    plt.scatter(
        [item["duration"] for item in result["result"]],
        [item["ratio"] for item in result["result"]],
    )
    plt.xlabel("audio duration")
    plt.ylabel("ratio")
    plt.savefig(f"{save_dir}/compare_ratio.png")


def get_audio_info(url: str):
    """获取音频信息"""
    response = requests.get(url)
    audio = BytesIO(response.content)
    y, sr = librosa.load(audio, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    return round(duration, 2), sr
