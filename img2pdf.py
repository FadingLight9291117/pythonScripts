from PIL import Image
from pathlib import Path
import argparse


def img2pdf(img_path, save_path):
    save_path = Path(save_path)
    if type(img_path) == str:
        img_path = Path(img_path)
        img = Image.open(img_path).convert("RGB")

        img.save(save_path.with_suffix('.pdf'), "PDF",
                 resolutions=100.0, save_all=True)

    elif type(img_path) == list and img_path.__len__() > 0:
        img_path = [Path(path) for path in img_path]

        img0_path = img_path.pop(0)
        img0 = Image.open(img0_path)

        imgs = []

        for path in img_path:
            img = Image.open(path).convert("RGB")
            imgs.append(img)

        img0.save(save_path.with_suffix('.pdf'), "PDF",
                  resolutions=100., save_all=True, append_images=imgs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-path', required=True, type=str, help="输入图像文件的路径")
    parser.add_argument('--save-path', default="", type=str, help="输入pdf的保存路径，默认保存在图像同目录同名")

    args = parser.parse_args()
    
    img_path = args.img_path
    save_path = args.save_path
    if save_path == "":
        save_path = Path(img_path).with_suffix('.pdf')
    img2pdf(img_path, save_path)