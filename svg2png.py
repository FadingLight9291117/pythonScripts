import cairosvg
from PIL import Image

svg_file = "input.svg"
png_file = "output.png"

output_width = 160
output_height = 160

cairosvg.svg2png(url=svg_file, write_to=png_file,
                 output_width=output_width, output_height=output_height)

image = Image.open(png_file)

# 裁剪 PNG 图片的空白像素
image = image.crop(image.getbbox())

# 保存裁剪后的 PNG 图片
image.save(png_file)
