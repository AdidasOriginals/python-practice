#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/6 18:58 
# @Author : Edison
# @Version：V 0.1
# @File : test-022.py
# @desc :Python标准库初探
print('-' * 20, 'base64 - Base64编解码模块', '-' * 20)
import base64

content = 'supreme'
print(base64.b64encode(content.encode()))
content64 = b'c3VwcmVtZQ=='
print(base64.b64decode(content64).decode())
print('_' * 100)
from collections import namedtuple

Card = namedtuple('Card', ('suite', 'face'))
card1 = Card('红桃', 5)
card2 = Card('草花', 9)
print(f'{card1.suite}{card1.face}')
print(f'{card2.suite}{card2.face}')
print('-' * 20, 'collections - 容器数据类型模块', '-' * 20)
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
# 打印words列表中出现频率最高的3个元素及其出现次数
for elem, count in counter.most_common(3):
    print(elem, count)
print('-' * 20, 'hashlib - 哈希函数模块', '-' * 20)
import hashlib

# 计算字符串"123456"的MD5摘要
print('123456的md5摘要:', hashlib.md5('123456'.encode()).hexdigest())
# 计算文件"python-3.9.1-amd64.exe"的MD5摘要
# rb表示读取二进制文件 512表示字节数，默认为-1表示读取整个文件
# update 用提供的字节串更新此哈希对象(hash object)的状态
# hexdigest 返回摘要值,以十六进制数字字符串的形式。
hasher = hashlib.md5()
with open('E:\下载\python-3.9.1-amd64.exe', 'rb') as file:
    data = file.read(512)
    while data:
        hasher.update(data)
        data = file.read(512)
print(hasher.hexdigest())
print('-' * 20, 'heapq - 堆排序模块', '-' * 20)
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# 找出列表中最大的三个元素
print(heapq.nlargest(3, list1))
# 找出列表中最小的三个元素
print(heapq.nsmallest(3, list1))
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 找出价格最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# 找出持有数量最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['shares']))
print('-' * 20, 'itertools - 迭代工具模块', '-' * 20)
import itertools

# 产生ABCD的全排列
print('-' * 20, '产生ABCD的全排列', '-' * 20)
for value in itertools.permutations('ABCD'):
    print(value)
# 产生ABCDE的五选三组合
print('-' * 20, '产生ABCDE的五选三组合', '-' * 20)
for value in itertools.combinations('ABCDE', 3):
    print(value)
# 产生ABCD和123的笛卡尔积
print('-' * 20, '产生ABCD和123的笛卡尔积', '-' * 20)
for value in itertools.product('ABCD', '123'):
    print(value)
# 产生ABC的无限循环序列
print('-' * 20, '产生ABC的无限循环序列', '-' * 20)
it = itertools.cycle(('A', 'B', 'C'))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print('-' * 20, 'random - 随机数和随机抽样模块', '-' * 20)
import random
import matplotlib.pyplot as plt
import seaborn as sns

# getrandbits(k)：返回具有k个随机比特位的整数。
print(random.getrandbits(2))
# randrange(start, stop[, step])：从range(start, stop, step) 返回一个随机选择的元素，但实际上并没有构建一个range对象。
print(random.randrange(1, 10, 2))
# randint(a, b)：返回随机整数N满足a <= N <= b，相当于randrange(a, b+1)。
print(random.randint(6, 8))
# choice(seq)：从非空序列seq返回一个随机元素。 如果seq为空，则引发IndexError。
print(random.choice(['666', '888']))
# choices(population, weight=None, *, cum_weights=None, k=1)：从population中选择替换，返回大小为k的元素列表。 如果population为空，则引发IndexError。
list = [1, 2, 3, 4, 5]
print(random.choices(list, k=5))
print(random.choices(list, weights=[0, 0, 1, 0, 0], k=5))
print(random.choices(list, weights=[1, 1, 1, 1, 1], k=5))
print(random.choices(list, cum_weights=[1, 1, 1, 1, 1], k=5))
# 1 ： 重复输出10次列表a中的各个成员出现概率基本持平。
# 2 ： 重复输出10次每次输出均得到[3,3,3,3,3]结果。
# 3 ： 重复输出10次列表a中的各个成员出现概率基本持平。
# 4 ： 重复输出10次每次输出均得到[1,1,1,1,1]结果。
# shuffle(x[, random])：将序列x随机打乱位置。没有返回值
random.shuffle(list)
print(list)
random.shuffle(list)
print(list)
# sample(population, k)：返回从总体序列或集合中选择k个不重复元素构造的列表，用于无重复的随机抽样。
print(random.sample(list, 3))
# random()：返回[0.0, 1.0)范围内的下一个随机浮点数。
print(random.random())
# expovariate(lambd)：指数分布。
# seaborn是基于matplotlib进行的更上一层的封装，需要借助matplotlib中的pyplot 进行展示图片 plt.show()
data = [random.expovariate(2) for i in range(50000)]
# 直方图
plt.hist(data, bins=100, color="#FF0000", alpha=.7)
# plt.show()
# 密度图
sns.kdeplot(data, shade=True, color="#FF0000")
# plt.show()
# gammavariate(alpha, beta)：伽玛分布。
data = [random.gammavariate(2, 2) for i in range(50000)]
# 直方图
plt.hist(data, bins=100, color="#FF0000", alpha=.7)
# plt.show()
# 密度图
sns.kdeplot(data, shade=True, color="#FF0000")
# plt.show()
# gauss(mu, sigma) / normalvariate(mu, sigma)：正态分布。
data = [random.gauss(2, 2) for i in range(50000)]
# 直方图
plt.hist(data, bins=100, color="#FF0000", alpha=.7)
# plt.show()
# 密度图
sns.kdeplot(data, shade=True, color="#FF0000")
# plt.show()
# paretovariate(alpha)：帕累托分布。
data = [random.paretovariate(4) for i in range(50000)]
# 直方图
plt.hist(data, bins=100, color="#FF0000", alpha=.7)
# plt.show()
# 密度图
sns.kdeplot(data, shade=True, color="#FF0000")
# plt.show()
# weibullvariate(alpha, beta)：威布尔分布。
data = [random.weibullvariate(1, 2) for i in range(20000)]
# 直方图
plt.hist(data, bins=100, color="#FF0000", alpha=.7)
# plt.show()
sns.kdeplot(data, shade=True, color="#FF0000")
# plt.show()
print('-' * 20, 'os.path - 路径操作相关模块', '-' * 20)
import os

# dirname(path)：返回路径path的目录名称。
path = 'python.txt'
print(os.getcwd())
print(os.path.dirname(path))
# exists(path)：如果path指向一个已存在的路径或已打开的文件描述符，返回 True。
print(os.path.exists(path))
# getatime(path) / getmtime(path) / getctime(path)：返回path的最后访问时间/最后修改时间/创建时间。
print(os.path.getatime(path))  # 输出最近访问时间
print(os.path.getctime(path))  # 输出文件创建时间
print(os.path.getmtime(path))  # 输出最近修改时间
# getsize(path)：返回path的大小，以字节为单位。如果该文件不存在或不可访问，则抛出OSError异常。
print(os.path.getsize(path))  # 输出文件大小（字节为单位）
# isfile(path)：如果path是普通文件，则返回 True。
print(os.path.isfile(path))
# isdir(path)：如果path是目录（文件夹），则返回True。
print(os.path.isdir(path))
# join(path, *paths)：合理地拼接一个或多个路径部分。返回值是path和paths所有值的连接，
# 每个非空部分后面都紧跟一个目录分隔符 (os.sep)，除了最后一部分。这意味着如果最后一部分为空，则结果将以分隔符结尾。
# 如果参数中某个部分是绝对路径，则绝对路径前的路径都将被丢弃，并从绝对路径部分开始连接。
print(os.path.join('test', 'test.txt'))  # 将目录和文件名合成一个路径
# splitext(path)：将路径path拆分为一对，即(root, ext)，使得root + ext == path，其中ext为空或以英文句点开头，且最多包含一个句点。
print(os.path.splitext(path))  # 分割路径，返回路径名和文件扩展名的元组
print(os.path.split(path))  # 分割文件名与路径
print('-' * 20, 'uuid - UUID生成模块', '-' * 20)
# uuid1()：由MAC地址、当前时间戳、随机数生成，可以保证全球范围内的唯一性。
# uuid3(namespace, name)：通过计算命名空间和名字的MD5哈希摘要（“指纹”）值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字会生成相同的UUID。
# uuid4()：由伪随机数生成UUID，有一定的重复概率，该概率可以计算出来。
# uuid5()：算法与uuid3相同，只不过哈希函数用SHA-1取代了MD5。
import uuid

name = 'python'
namespace = uuid.uuid1()
print(uuid.uuid1())
print(uuid.uuid3(uuid.uuid1(), name))
print(uuid.uuid4())
print(uuid.uuid5(namespace, name))
