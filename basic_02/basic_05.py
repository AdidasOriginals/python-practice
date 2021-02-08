#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/8 17:19 
# @Author : Edison 
# @Version：V 0.1
# @File : basic_05.py
# @desc : 迭代器和生成器
print('迭代器和生成器'.center(50, '*'))
print('迭代器'.center(50, '-'))


class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


d = Fib(10)

for val in d:
    print(val)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())

print('生成器'.center(50, '-'))


def fib2(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


f = fib2(3)
print(f.__next__())
print(f.__next__())
print(f.__next__())
# 当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。
# print(f.__next__())
for val in fib2(10):
    print(val)
print('生成器进化为协程'.center(50, '-'))


def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))
