import cairosvg
from pathlib import Path
import argparse
from PIL import Image


def svg2png(svg_path, save_path, output_size: tuple = (160, 160)):
    output_width, output_height = output_size
    cairosvg.svg2png(url=svg_path, write_to=save_path, output_width=output_width, output_height=output_height)

    image = Image.open(save_path)

    # 保存裁剪后的 PNG 图片
    image.save(save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--svg_path', type=str, help='svg图片路径', required=True)
    parser.add_argument('-s', '--save_path', type=str, help='png保存路径默认保存到svg路径下', required=False)
    parser.add_argument('--output_width', type=int, default=160, help='输出png的width')
    parser.add_argument('--output_height', type=int, default=160, help='输出png的height')

    args = parser.parse_args()

    svg2png(
        svg_path=args.svg_path,
        save_path=args.save_path if args.save_path else str(Path(args.svg_path).parent / 'result.png'),
        output_size=(args.output_width, args.output_height),
    )
