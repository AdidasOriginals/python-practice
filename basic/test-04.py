#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/15 11:30 
# @Author : Edison
# @Version：V 0.1
# @File : test-04.py
# @desc :循环结构
print('-' * 20, 'for-in循环', '-' * 20)
sum = 0
for x in range(101):
    sum += x
print(sum)
# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
"""
用for循环实现1~100之间的偶数求和

Version: 0.1
"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
# 相较于上面直接跳过奇数的做法，下面这种做法很明显并不是很好的选择
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
print('-' * 20, 'while循环', '-' * 20)
"""
猜数字游戏

Version: 0.1
"""
import random

answer = random.randint(1, 100)
print(answer)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
"""
输出乘法口诀表(九九表)

Version: 0.1
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
"""
输入一个正整数判断它是不是素数

Version: 0.1
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
"""
输入两个正整数计算它们的最大公约数和最小公倍数

Version: 0.1
"""

# x = int(input('x = '))
# y = int(input('y = '))
x = 10
y = 8
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
"""
打印三角形图案

Version: 0.1
"""

row = int(input('请输入行数: '))
print()
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
