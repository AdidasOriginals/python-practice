# coding=utf-8
# -*- coding: UTF-8 -*-
print('*' * 20, '函数的高级应用', '*' * 20)
print('-' * 10, '装饰器', '-' * 10)
import random
import time


def download(filename):
    print(f'开始下载{filename}')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成')


def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成')


# 执行
# download('mysql从删库到跑路.avi')
# upload('python从入门到住院.pdf')
import time


# 定义装饰器函数，它的参数是被装饰的函数或类
def record_time(func):
    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # 在Python中函数可以嵌套的定义（函数中可以再定义函数）
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间:{end - start:.3f}秒')
        # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
        return result

    # 返回带装饰功能的wrapper函数
    return wrapper


# 直接调用装饰器函数，传入被装饰的函数并获得返回值，我们可以用这个返回值直接覆盖原来的函数，
# 那么在调用时就已经获得了装饰器提供的额外的功能（记录执行时间）
download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
print('-' * 30)
import random
import time


def record_time2(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        return result

    return wrapper


@record_time2
def download2(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


@record_time2
def upload2(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


download2('2-MySQL从删库到跑路.avi')
upload2('2-Python从入门到住院.pdf')
print('-' * 30)
import random
import time

from functools import wraps


def record_time3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        return result

    return wrapper


@record_time3
def download3(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


@record_time3
def upload3(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


# Python标准库functools模块的wraps函数也是一个装饰器，我们将它放在wrapper函数上，这个装饰器可以帮我们保留被装饰之前的函数，
# 这样在需要取消装饰器时，可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数
download3('3-MySQL从删库到跑路.avi')
upload3('3-Python从入门到住院.pdf')
# 取消装饰器
download3.__wrapped__('3-MySQL必知必会.pdf')
upload3 = upload3.__wrapped__
upload3('3-Python从新手到大师.pdf')
print('-' * 30)


class RecordTime:

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'{func.__name__}执行时间: {end - start:.3f}秒')
            return result

        return wrapper


# 使用装饰器语法糖添加装饰器
@RecordTime()
def download4(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload4(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


# 直接创建对象并调用对象传入被装饰的函数
upload4 = RecordTime()(upload4)
download4('4-MySQL从删库到跑路.avi')
upload4('4-Python从入门到住院.pdf')
print('-' * 30)
print('-' * 10, '递归调用', '-' * 10)


# 递归阶乘
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


print(fac(5))  # 120


# 递归计算 斐波那契数列第N个数
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


# 打印前20个斐波那契数(执行性能比较糟糕)
for i in range(0, 21):
    print(fib(i))


# 循环递归 斐波那契数列第N个数的值
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib2(20))  # 6765
