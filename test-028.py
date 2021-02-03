#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/14 15:05 
# @Author : Edison
# @Version：V 0.1
# @File : test-028.py
# @desc :用Python读写Excel文件
print('-' * 20, '使用xlwt和xlrd', '-' * 20)
import xlrd
import random
import xlwt
from xlutils.copy import copy

print('-' * 20, '读Excel文件', '-' * 20)
# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb = xlrd.open_workbook('data/read.xlsx')
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetname = wb.sheet_names()[0]
# 通过指定的表单名称获取Sheet对象（工作表）
sheet = wb.sheet_by_name(sheetname)
# 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
print(sheet.nrows, sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
            # 第1列的xldate类型先转成元组再格式化为“年月日”的格式
            if col == 0:
                # xldate_as_tuple函数的第二个参数只有0和1两个取值
                # 其中0代表以1900-01-01为基准的日期，1代表以1904-01-01为基准的日期
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            elif col == 2:
                value = f'{value:.2f}'
            else:
                value = value
        print(value, end='\t')
    print()
# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)
# 获取第一行的值（列表）
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 5))
print('-' * 20, '写Excel文件', '-' * 20)

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randint(40, 100) for _ in range(3)] for _ in range(len(student_names))]
# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()
# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班', cell_overwrite_ok=True)
# 添加表头数据
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title)
# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
# 保存Excel工作簿
# wb.save('./data/student_grades.xlsx')
print('-' * 20, '调整单元格样式', '-' * 20)
print('设置表头背景颜色')
header_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色、
pattern.pattern_fore_colour = 5
header_style.pattern = pattern
print('设置表头指定字体')
font = xlwt.Font()
# 字体名称
font.name = '华文楷体'
# 字体大小（20是基准单位，18表示18px）
font.height = 20 * 18
# 是否使用粗体
font.bold = True
# 是否使用斜体
font.italic = False
# 字体颜色
font.colour_index = 2
header_style.font = font
print('表头垂直居中对齐')
align = xlwt.Alignment()
# 垂直方向的对齐方式
align.vert = xlwt.Alignment.VERT_CENTER
# 水平方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align
print('表头加黄色虚线边框')
borders = xlwt.Borders()
props = (
    ('top', 'top_colour'), ('right', 'right_colour'),
    ('bottom', 'bottom_colour'), ('left', 'left_colour')
)
# 通过循环对四个方向的边框样式及颜色进行设定
for position, color in props:
    setattr(borders, position, xlwt.Borders.DASHED)
    setattr(borders, color, 5)
header_style.borders = borders
print('调整单元格的宽度（列宽）和表头的高度（行高）')
# 设置行高为40px
sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    # 设置列宽为200px
    sheet.col(index).width = 20 * 200
    sheet.write(0, index, title, header_style)
wb.save('./data/test2.xlsx')
print('-' * 20, '公式计算', '-' * 20)
wb_for_read = xlrd.open_workbook('./data/read.xlsx')
sheet1 = wb_for_read.sheet_by_index(0)
nrows, ncols = sheet1.nrows, sheet1.ncols
wb_for_write = copy(wb_for_read)
sheet2 = wb_for_write.get_sheet(0)
sheet2.write(nrows, 2, xlwt.Formula(f'average(C2:C{nrows})'))
sheet2.write(nrows, 3, xlwt.Formula(f'sum(D2:D{nrows})'))
wb_for_write.save('./data/test3.xlsx')
