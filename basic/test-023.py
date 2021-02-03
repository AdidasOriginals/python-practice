#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/7 17:04 
# @Author : Edison
# @Version：V 0.1
# @File : test-023.py
# @desc :文件读写和异常处理
print('-' * 20, '打开和关闭文件', '-' * 20)
import sys
import time

# 当前系统默认的编码
print(sys.getdefaultencoding())
file = open('python.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
print('-' * 20, '逐行读取文本', '-' * 20)
# for-in
file2 = open('python.txt', 'r', encoding='utf-8')
for line in file2:
    print(line, end='')
    time.sleep(0.5)
file2.close()
print()
# readlines
file3 = open('python.txt', 'r', encoding='utf-8')
lines = file3.readlines()
for line in lines:
    print(line, end='')
    time.sleep(0.5)
file3.close()
file4 = open('python.txt', 'a', encoding='utf-8')
file4.write('\n4、第四行')
file4.close()
content = ['5、第五行', '6、第六行']
file5 = open('python.txt', 'a', encoding='utf-8')
for line in content:
    file5.write(f'\n{line}')
file5.close()
print()
print('-' * 20, '异常处理机制', '-' * 20)
file = None


# try:
#     file = open('致橡树.txt', 'r', encoding='utf-8')
#     print(file.read())
# except FileNotFoundError:
#     print('无法打开指定的文件！')
# except LookupError:
#     print('指定了未知的编码')
# except UnicodeDecodeError:
#     print('读取文件时编码错误！')
# finally:
#     if file:
#         file.close()


class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    """求阶乘"""
    if type(num) != int or num < 0:
        raise InputError('只能计算非负整数的阶乘！！！')
    if num in (0, 1):
        return 1
    return num * fac(nuprint(m - 1))


flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)

print('-' * 20, '上下文语法', '-' * 20)
# 对于open函数返回的文件对象，还可以使用with上下文语法在文件操作完成后自动执行文件对象的close方法
try:
    with open('致橡树.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
print('-' * 20, '读写二进制文件', '-' * 20)
try:
    with open('dog.jpg', 'rb') as file1:
        data = file1.read()
    with open('dogcopy.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开')
except IOError:
    print('读写文件时出现错误')
print('程序执行结束')

try:
    with open('dog.jpg', 'rb') as file1, \
            open('dogcopy2.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开')
except IOError:
    print('读写文件时出现错误')
print('程序执行结束')
