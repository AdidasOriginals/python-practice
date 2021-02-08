#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/5 11:25 
# @Author : Edison 
# @Version：V 0.1
# @File : basic_03.py
# @desc : 函数的使用方式
print('高阶函数的用法（filter、map以及它们的替代品）'.center(50, '*'))
items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
print(items1)
# x%2 取余结果为0是false，所以[1, 3, 5, 7, 9]为true
items2 = [x ** 2 for x in range(1, 10) if x % 2]
print(items2)
# Python搜索变量的LEGB顺序（Local >>> Embedded >>> Global >>> Built-in）
print('输出函数执行时间的装饰器'.center(50, '*'))
from functools import wraps
import time
import random


def record_time(func):
    """自定义装饰函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}:{time.time() - start:.3f}秒')
        return result

    return wrapper


# 使用装饰器语法糖添加装饰器
@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


# download('吉祥如意')

# 如果装饰器不希望跟print函数耦合，可以编写可以参数化的装饰器
def record(output):
    """可以参数化的装饰器"""

    # 装饰器工厂函数
    def decorate(func):
        # 真正的装饰器
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            output(func.__name__, f'{time.time() - start:.3f}')
            return result

        # 真正的装饰器
        return wrapper

    # 装饰器工厂函数
    return decorate


# 必须加参数才会返回真正的装饰器，不然不起作用
@record(print)
def download2(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


# download2('招财进宝')
class Record2():
    """通过定义类的方式定义装饰器"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            self.output(func.__name__, f'{time.time() - start:.3f}')
            return result

        return wrapper


@Record2(print)
def download3(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


# download3('健康快乐')
# 由于对带装饰功能的函数添加了@wraps装饰器，可以通过func.__wrapped__方式获得被装饰之前的函数或类来取消装饰器的作用
# download3.__wrapped__('取消装饰器-3')

print('用装饰器来实现单例模式'.center(50, '*'))
from functools import wraps


# cls 值得是作为参数传入的 类对象，此例中为 President
# 线程不安全的
def singleton(cls):
    """装饰类的装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        # 实例化cls对象，并存入instance中
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    """总统(单例类)"""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


# id一致
def main():
    print(President.__name__)
    p1 = President('特朗普', '美国')
    p2 = President('奥巴马', '美国')
    print(id(p1))
    print(id(p2))
    print(p1 == p2)
    print(p1)
    print(p2)


main()

# 线程安全的单例装饰器。
from functools import wraps
from threading import RLock


def singleton2(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
