#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/13 17:46 
# @Author : Edison
# @Version：V 0.1
# @File : test-026.py
# @desc :用Python处理图像
print('-' * 20, '用Pillow处理图像', '-' * 20)
from PIL import Image

# 1.读取和显示图像
# 读取图像获取image对象
image = Image.open('./image/dogcopy2.jpg')
# 通过image对象的format属性获取图像的格式
print(image.format)  # JPEG
# 通过image对象的size属性获取图像尺寸
print(image.size)  # (440, 418)
# 通过image对象的mode属性获取图像的模式
print(image.mode)  # RGB
# 通过image对象的show方法显示图像
# image.show()
# 2.剪裁图像
# 通过Image对象的crop方法指定剪裁区域剪裁图像
image.crop((80, 20, 310, 360))
# image.show()
# 3.生成缩略图
# 通过Image对象的thumbnail方法生成指定尺寸的缩略图
image.thumbnail((128, 128))
# image.show()
# 4.缩放和黏贴图像
# 读取照片1获得Image对象
dog_image = Image.open('./image/dogcopy.jpg')
# 读取照片2获得Image对象
dog2_image = Image.open('./image/dog2.jpg')
dog_head = dog_image.crop((0, 0, 440, 418))
width, height = dog_head.size
# 使用Image对象的resize方法修改图像的尺寸
# 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
dog2_image.paste(dog_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
# dog2_image.show()
# 5.旋转和翻转
image2 = Image.open('./image/dog2.jpg')
# 使用Image对象的rotate方法实现图像的旋转
image2.rotate(45)
# image2.show()
# 使用Image对象的transpose方法实现图像翻转
# Image.FLIP_LEFT_RIGHT - 水平翻转
# Image.FLIP_TOP_BOTTOM - 垂直翻转
image2.transpose(Image.FLIP_LEFT_RIGHT)
# image2.show()
# 6.操作像素
for x in range(80, 310):
    for y in range(20, 360):
        # 通过Image对象的putpixel方法修改图像指定像素点
        image2.putpixel((x, y), (128, 128, 128))
# image2.show()
# 7.滤镜效果
from PIL import ImageFilter

# 使用Image对象的filter方法对图像进行滤镜处理
# ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
image3 = Image.open('./image/dog2.jpg')
# image3.filter(ImageFilter.CONTOUR).show()
print('-' * 20, '使用Pillow绘图', '-' * 20)
import random
from PIL import Image, ImageDraw, ImageFont


def random_color():
    """生成随机颜色"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


width, height = 800, 600
# 创建一个800*600的图像，背景色为白色
image4 = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
# 创建一个ImageDraw对象
drawer = ImageDraw.Draw(image4)
# 通过指定字体和大小获得ImageFont对象
font = ImageFont.truetype('./fonts/Deng.ttf',32)
# 通过ImageDraw对象的text方法绘制文字
drawer.text((300, 50), 'Hello,World!', fill=(255, 0, 0), font=font)
# 通过ImageDraw对象的line方法绘制两条对角直线
drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)
drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)
xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60
# 通过ImageDraw对象的rectangle方法绘制矩形
drawer.rectangle(xy, outline=(255, 0, 0), width=2)
# 通过ImageDraw对象的ellipse方法绘制椭圆
for i in range(4):
    left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
    drawer.ellipse((left, top, right, bottom), outline=random_color(), width=8)
# 显示图像
image4.show()
# 保存图像
image4.save('./image/result.png')
