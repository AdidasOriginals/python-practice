#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/18 14:07 
# @Author : Edison
# @Version：V 0.1
# @File : test-07.py
# @desc :字符串和常用数据结构
print('-' * 20, '使用字符串', '-' * 20)
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u4e2d\u56fd'
print(s1, s2)
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world
print('ll' in s1)  # True
print('good' in s1)  # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45  负3到负一
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  testpython@python.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
print('使用列表'.center(50, '-'))
list1 = [1, 3, 5, 7, 100]
print(list1)  # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2)  # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1))  # 5
# 下标(索引)运算
print(list1[0])  # 1
print(list1[4])  # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])  # 100
print(list1[-3])  # 5
list1[2] = 300
print(list1)  # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1))  # 9
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)  # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1)  # []
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)  # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)  # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)  # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list2)  # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
print(list3)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list4)  # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)  # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print('生成式和生成器'.center(50, '-'))
import sys

f = [x for x in range(1, 10)]
print(f)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [x + y for x in 'ABCDE' for y in '1234567']
# ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5',
# 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
# 查看对象占用内存的字节数（列表）
print(sys.getsizeof(f))  # 8856
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, ...998001]
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
# 相比生成式生成器不占用存储数据的空间 （元组）
print(sys.getsizeof(f))  # 112
# 生成器对象 <generator object <genexpr> at 0x00000276909EE5F0>
print(f)
# 1,4,9,16,25,36,49,64,81,100,121,144,169,196...998001
for val in f:
    print(val, end=',')


# 获取前N个斐波那契数列
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


main()
print('----------------')
f = fib(3)
print(f.__next__())
print(f.__next__())
print(f.__next__())
# 当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。
# print(f.__next__())
print('----------------')
print('使用元组'.center(50, '-'))
# 元组在创建时间和占用的空间上面都优于列表
# 定义元组
t = ('吴彦祖', 47, True, '美国旧金山')
# ('吴彦祖', 47, True, '美国旧金山')
print(t)
# 获取元组中的元素
print(t[0])  # 吴彦祖
print(t[3])  # 美国旧金山
# 遍历元组中的值
# 吴彦祖
# 47
# True
# 美国旧金山
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
# ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
# ['王大锤', 20, True, '云南昆明']
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
# ['李小龙', 25, True, '云南昆明']
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
# ('apple', 'banana', 'orange')
print(fruits_tuple)
print('使用集合'.center(50, '-'))
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
# {1, 2, 3}
print(set1)
# Length = 3
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
# {1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3}
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# {3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65,
# 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99}
print(set4)
# 添加元素，如果元素已存在，则不进行任何操作
set1.add(4)
set1.add(5)
# 添加元素，且参数可以是列表，元组，字典等
set2.update([11, 12])
# 移除集合中的元素，且如果元素不存在，不会发生错误
set2.discard(5)
if 4 in set2:
    # 如果元素不存在，则会发生错误
    set2.remove(4)
# {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12}
print(set1, set2)
# pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
# pop() 方法用于随机移除一个元素。
print(set3.pop())  # 1
# {2, 3}
print(set3)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)  # {1, 2, 3}
# print(set1.intersection(set2))
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
# print(set1.union(set2))
print(set1 - set2)  # {4, 5}
# print(set1.difference(set2))
print(set1 ^ set2)  # {4, 5, 6, 7, 8, 9, 11, 12}
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)  # False
# print(set2.issubset(set1))
print(set3 <= set1)  # True
# print(set3.issubset(set1))
print(set1 >= set2)  # False
# print(set1.issuperset(set2))
print(set1 >= set3)  # True
# print(set1.issuperset(set3))
print('使用字典'.center(50, '-'))
# 创建字典的字面量语法
scores = {'吴彦祖': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)  # {'吴彦祖': 95, '白元芳': 78, '狄仁杰': 82}
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))  # {'a': '1', 'b': '2', 'c': '3'}
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['吴彦祖'])  # 95
print(scores['狄仁杰'])  # 95
# 对字典中所有键值对进行遍历
# 吴彦祖: 95
# 白元芳: 78
# 狄仁杰: 82
for key in scores:
    print(f'{key}: {scores[key]}')
# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)  # {'吴彦祖': 95, '白元芳': 65, '狄仁杰': 82, '诸葛王朗': 71, '冷面': 67, '方启鹤': 85}
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))  # None
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))  # 60
# 删除字典中的元素
# popitem() 方法返回并删除字典中的最后一对键和值
print(scores.popitem())  # ('方启鹤', 85)
print(scores.popitem())  # ('冷面', 67)
# pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值
print(scores.pop('吴彦祖', 100))  # 95
# 清空字典
scores.clear()
print(scores)  # {}
print('在屏幕上显示跑马灯文字'.center(50, '-'))
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    print(content[1:])
    print(content[0])
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


# main()
print('生成指定长度的验证码'.center(50, '-'))
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


print(generate_code(4))
print('获取文件名的后缀名'.center(50, '-'))


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


print(get_suffix('test.mp4'))
print('列表中最大和第二大的元素的值'.center(50, '-'))


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


aaa = [1, 100, 88, 66]
print(max2([1, 100, 88, 66]))
print(aaa.sort(reverse=True))
print(aaa)
print(sorted([1, 100, 88, 66], reverse=True))
print('计算指定的年月日是这一年的第几天'.center(50, '-'))


def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


print(which_day(1980, 11, 28))
print(which_day(1981, 12, 31))
print(which_day(2018, 1, 1))
print(which_day(2016, 3, 1))
print(which_day(2021, 1, 20))
print('打印杨辉三角'.center(50, '-'))

triangle_num = 8


def yanghui_triangle():
    # num = int(input('请输入行数: '))
    yh = [[]] * triangle_num
    print(yh)
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


yanghui_triangle()


def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]


def test_triangles():
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == triangle_num:
            break


test_triangles()
import operator


def triangles2():
    b = [1]
    while True:
        yield b
        c = [0] + b
        d = b + [0]
        b = list(map(operator.add, c, d))


n = 0
for t in triangles2():
    print(t)
    n += 1
    if n == triangle_num:
        break
print('双色球选号'.center(50, '-'))
from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    # selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


# n = int(input('机选几注：'))
n = 3
print()
for _ in range(n):
    display(random_select())
print('约瑟夫环问题'.center(50, '-'))
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def josephus():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30

    for person in persons:
        print('基' if person else '非', end='')


josephus()
print('井字棋游戏'.center(50, '-'))
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main3():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


main3()
