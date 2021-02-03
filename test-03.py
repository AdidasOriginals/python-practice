#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/15 11:15 
# @Author : Edison
# @Version：V 0.1
# @File : test-03.py
# @desc :分支结构
print('-' * 20, 'if语句的使用', '-' * 20)
# username = input('请输入用户名: ')
# password = input('请输入口令: ')
username = 'admin'
password = '123456'
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
print('-' * 20, '多分支', '-' * 20)
# x = float(input('x = '))
x = 8
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
print('-' * 20, '多分支2', '-' * 20)
# x = float(input('x = '))
x = 8
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
print('-' * 20, '英制单位英寸与公制单位厘米互换', '-' * 20)
# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
value = 888
unit = 'cm'
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
print('-' * 20, '百分制成绩转换为等级制成绩', '-' * 20)
# score = float(input('请输入成绩: '))
score = 100
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
print('-' * 20, '输入三条边长，如果能构成三角形就计算周长和面积', '-' * 20)
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % area)
else:
    print('不能构成三角形')





