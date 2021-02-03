#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/15 16:43 
# @Author : Edison
# @Version：V 0.1
# @File : test-06.py
# @desc :函数和模块的使用
print('-' * 20, '函数的作用', '-' * 20)

"""
输入M和N计算C(M,N)

Version: 0.1
"""
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1, m - n + 1):
#     fm_n *= num
# print(fm // fn // fm_n)
"""
输入M和N计算C(M,N)

Version: 0.1
"""
import math


def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


# m = int(input('m = '))
# n = int(input('n = '))
# 八个苹果给4个小朋友分，每个人最少一个    C(M,N)(M=7,N=3)
m, n = 7, 3
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(fac(m) // fac(n) // fac(m - n))
print(math.factorial(m) // math.factorial(n) // math.factorial(m - n))
print('-' * 20, '函数的参数', '-' * 20)
from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
print('-' * 20, '用模块管理函数', '-' * 20)


def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？ #goodbye, world!
foo()
from main import foo

# 输出main-hello, world!

foo()
from test import foo

# 输出test-goodbye, world!
foo()
import main as m1
import test as m2

# main,hello, world!
m1.foo()
# test,goodbye, world!
m2.foo()
# 程序中调用的是最后导入的那个foo，因为后导入的foo覆盖了之前导入的foo
from main import foo
from test import foo

# 输出test-goodbye, world!
foo()
print('-' * 20, '求最大公约数和最小公倍数的函数', '-' * 20)


def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


print(gcd(8, 12))
print(lcm(18, 30))
print('-' * 20, '判断一个数是不是回文数的函数', '-' * 20)


# 设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。
# 例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


print(is_palindrome(1221))
print('-' * 20, '判断一个数是不是素数的函数', '-' * 20)


# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数
# ** 0.5 开平方
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


print(is_prime(3))
# 11，101，131，151，181，191，313，353，373，383，727，757，787，797，919，929
print('-' * 20, '判断输入的正整数是不是回文素数', '-' * 20)
# num = int(input('请输入正整数: '))
num = 11
if is_palindrome(num) and is_prime(num):
    print('%d是回文素数' % num)
else:
    print(f'不是回文素数:{num}')
print('-' * 20, '变量的作用域', '-' * 20)


# 由内而外查找变量顺序：局部作用域、嵌套作用域、全局作用域、内置作用域（input、print、int）
def foo():
    # 局部变量（local variable），属于局部作用域
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        # 局部作用域
        c = True
        print(a)
        # 嵌套作用域
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


# 全局变量（global variable），属于全局作用域
a = 100
# print(b)  # NameError: name 'b' is not defined
foo()


def foo2():
    # 局部变量
    a2 = 200
    print(a2)  # 200


a2 = 100
foo2()
print(a2)  # 100


# global关键字指示变量a3来自于全局作用域
def foo3():
    # 全局变量
    global a3
    a3 = 200
    print(a3)  # 200


a3 = 100
foo3()
print(a3)  # 200


# nonlocal关键字来指示变量来自于嵌套作用域
def foo4():
    # 全局变量
    a4 = 200
    print(a4)  # 200

    def foo5():
        nonlocal a4
        a4 += 100
        print(a4)

    foo5()


foo4()
