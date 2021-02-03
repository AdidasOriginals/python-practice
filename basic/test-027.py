#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/14 11:38 
# @Author : Edison
# @Version：V 0.1
# @File : test-027.py
# @desc :用Python读写CSV文件
print('-' * 20, '将数据写入CSV文件', '-' * 20)
import csv
import random

with open('data/scores.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    # delimiter 指定分隔符（默认是逗号）
    # quotechar 包围值的字符（默认是双引号）
    # quoting 包围的方式
    # writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for i in range(len(names)):
        verbal = random.randint(50, 100)
        math = random.randint(40, 100)
        english = random.randint(30, 100)
        writer.writerow([names[i], verbal, math, english])
print('-' * 20, '从CSV文件读取数据', '-' * 20)
with open('data/scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='|')
    for line in reader:
        print(reader.line_num, end='\t')
        for elem in line:
            print(elem, end='\t')
        print()
