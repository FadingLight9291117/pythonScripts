import argparse
from img2pdf import img2pdf

"""
    做成所有脚本的入口，然后将这个文件暴露给环境环境变量

    python pythonTools.py --task svg2png --args xxx
"""

task_map = dict(
    img2pdf=img2pdf,
    # svg2png=svg2png,
)


def select_task(task_name: str, params: dict):
    task = task_map[task_name]
    task(**params)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', type=str, help='选择要执行的任务', required=True)

    args = parser.parse_args()
    args = dict(args.__dict__)

    print(args)
