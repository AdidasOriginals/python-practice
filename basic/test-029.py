#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/14 16:33 
# @Author : Edison
# @Version：V 0.1
# @File : test-029.py
# @desc :用Python操作PDF文件
print('-' * 20, '从PDF中提取文本', '-' * 20)
import PyPDF2

reader = PyPDF2.PdfFileReader('./data/read_pdf.pdf')
# filename = open('C:/Users/46040/Desktop/Nova_Cinema_CGV_AGRU_Signed and notarized by TT & LL2.pdf','rb')
# reader = PyPDF2.PdfFileReader(filename)
print(reader.getNumPages())
for i in range(0, reader.getNumPages()):
    print(reader.getPage(i).extractText())

print('-' * 20, '旋转和叠加页面', '-' * 20)
reader = PyPDF2.PdfFileReader('./data/read_pdf.pdf')
page = reader.getPage(0)
page.rotateClockwise(90)
writer = PyPDF2.PdfFileWriter()
writer.addPage(page)
with open('data/write_pdf.pdf', 'wb') as file:
    writer.write(file)
print('-' * 20, '加密PDF文件', '-' * 20)
with open('data/demo.pdf', 'rb')as file:
    # 通过PdfReader读取未加密的PDF文档
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    for page_num in range(reader.getNumPages()):
        # 通过PdfReader的getPage方法获取指定页码的页
        # 通过PdfWriter方法的addPage将添加读取到的页
        writer.addPage(reader.getPage(page_num))
    # 通过PdfWriter的encrypt方法加密PDF文档
    writer.encrypt('dog')
    # 将加密后的PDF文档写入指定的文件中
    with open('data/write_pdf3.pdf', 'wb') as file2:
        writer.write(file2)
print('-' * 20, '创建PDF文件', '-' * 20)
import random
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 注册字体
# pdfmetrics.registerFont(TTFont('STSONG', './STSONG.TTF'))
pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))
# 创建Canvas对象（PDF文档对象）
doc = canvas.Canvas('data/demo.pdf', pagesize=A4)
# 获取A4纸的尺寸
width, height = A4
print(width, height)
# 读取图像
image = canvas.ImageReader('image/dog2.jpg')
# 通过PDF文档对象的drawImage绘制图像内容
doc.drawImage(image, 50, 200, 500, 400)
# 设置字体和颜色
# doc.setFont('Helvetica', 32)
# 使用新字体-支持中文
doc.setFont("SimSun", 32)
doc.setFillColorRGB(0.8, 0.4, 0.2)
# 通过PDF文档对象的drawString输出字符串内容
doc.drawString(150, 700, "这是一只可爱的狗子")
# 保存当前页创建新页面
doc.showPage()
# 准备表格需要的数据
# table中文乱码
scores = [[random.randint(60, 100) for _ in range(3)] for _ in range(5)]
names = ('旺财', '来福', '招财', '进宝', '发财')
for row, name in enumerate(names):
    scores[row].insert(0, name)
scores.insert(0, ['名字', '智商', '体重', '身长'])
# 创建一个Table对象（第一个参数是数据，第二个和第三个参数是列宽和行高）
table = Table(scores, 50, 20)
# 设置表格样式（对齐方式和内外边框粗细颜色）
table.setStyle(TableStyle(
    [
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.red),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
    ]
))
table.split(0, 0)
# 通过Table对象的drawOn在PDF文档上绘制表格
table.drawOn(doc, (width - 200) // 2, height - 150)
# 保存当前页创建新页面
doc.showPage()
# 保存PDF文档
doc.save()


def write_pdf():
    # 注册字体
    pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))
    c = canvas.Canvas("demo1.pdf")
    # 应用注册的字体
    c.setFont("SimSun", 14)
    c.drawString(200, 550, "自从PDF支持中文以后，整个人都变了")
    c.save()

# write_pdf()
