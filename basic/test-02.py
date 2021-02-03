#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/15 11:01 
# @Author : Edison
# @Version：V 0.1
# @File : test-01.py
# @desc :语言元素
print('-' * 20, '变量的使用', '-' * 20)

a = 321
b = 12
print(a + b)  # 333
print(a - b)  # 309
print(a * b)  # 3852
print(a / b)  # 26.75

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>

# a = int(input('a = '))
# b = int(input('b = '))
a = 8
b = 8
print()
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
print('-' * 20, '运算符', '-' * 20)
a = 10
b = 3
a += b  # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)
print(a)  # 算一下这里会输出什么 13 * 15 =195
print('-' * 20, '比较运算符和逻辑运算符', '-' * 20)
# 比较运算符的优先级高于赋值运算符
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)  # flag0 = True
print('flag1 =', flag1)  # flag1 = True
print('flag2 =', flag2)  # flag2 = False
print('flag3 =', flag3)  # flag3 = False
print('flag4 =', flag4)  # flag4 = True
print('flag5 =', flag5)  # flag5 = False
print('-' * 20, '比较运算符和逻辑运算符', '-' * 20)
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
print('-' * 20, '输入圆的半径计算计算周长和面积', '-' * 20)
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
print('-' * 20, '输入年份判断是不是闰年', '-' * 20)
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(f'{year}年是不是闰年：{is_leap}')
