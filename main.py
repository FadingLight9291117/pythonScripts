from PIL import Image

# 指定输入的 PNG 文件名和输出的 PNG 文件名
png_file = "./output.png"
output_file = "res.png"

# 打开 PNG 文件
image = Image.open(png_file)

# 裁剪 PNG 图片的空白像素
image = image.crop(image.getbbox())

# 保存裁剪后的 PNG 图片
image.save(output_file)