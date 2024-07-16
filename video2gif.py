from moviepy.editor import VideoFileClip
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, help='video path')
args = parser.parse_args()

# 读取视频文件
video_path = args.path
video = VideoFileClip(video_path)

# 将视频转换为 GIF 图
gif_path = Path(video_path).parent / 'output_gif.gif'
video.write_gif(gif_path, fps=10, fuzz=10)

print("视频转 GIF 完成！")
