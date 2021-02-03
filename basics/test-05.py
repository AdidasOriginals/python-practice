#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/15 14:03 
# @Author : Edison
# @Version：V 0.1
# @File : test-05.py
# @desc :构造程序逻辑
print('-' * 20, '经典的例子', '-' * 20)
"""
找出所有水仙花数

Version: 0.1
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
"""
正整数的反转

Version: 0.1
"""

# num = int(input('num = '))
num = 88888
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
"""
《百钱百鸡》问题

Version: 0.1
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

Version: 0.1
Author: 骆昊
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        # debt = int(input('请下注: '))
        debt = money
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')
"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
"""


# num = int(input('请输入要打印的斐波那契数量：'))
# print(num)

def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        print(a, end=' ')


fib(10)
"""
找出10000以内的完美数  1-9999
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""
import math
import datetime
import time

# 性能差
# start = datetime.datetime.now()
# for i in range(1, 10000):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     if i == sum:
#         print(i)
# end = datetime.datetime.now()
# #25秒
# print((end - start).seconds, '秒')
#一个数的最大因子也就是它的开平方数了
start = time.time()
for num in range(1, 29):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)

end = time.time()
print(end - start)
"""
输出100以内的素数   2-99
只能被1和自身整除的正整数
Version: 0.1
"""
for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
print()

