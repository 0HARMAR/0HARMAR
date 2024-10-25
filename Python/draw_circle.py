from PIL import Image, ImageDraw

# 定义图像尺寸和背景色
size = (200, 200)
background_color = (255, 255, 255, 0)  # 白色背景，透明度0（用于PNG）

# 创建一个带透明背景的图像
image = Image.new("RGBA", size, background_color)

# 创建一个绘图对象
draw = ImageDraw.Draw(image)

# 定义圆的颜色和位置
circle_color = (0, 0, 255, 255)  # 蓝色，完全不透明
circle_bbox = [20, 20, 180, 180]  # 圆形的边界框，左上角(x1, y1)，右下角(x2, y2)

# 绘制圆形
draw.ellipse(circle_bbox, fill=circle_color)

# 保存为 PNG 图片
image.save("circle.png", "PNG")

# 如果你需要保存成 JPG（JPG 不支持透明背景，因此使用白色背景）
image_jpg = Image.new("RGB", size, (255, 255, 255))  # 创建一个白色背景的图像
image_jpg.paste(image, (0, 0), image)  # 将圆形粘贴到白色背景上

# 保存为 JPG 图片
image_jpg.save("circle.jpg", "JPEG")

