#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/14 18:56 
# @Author : Edison
# @Version：V 0.1
# @File : test-030.py
# @desc :用Python获取网络数据
import resp as resp

print('-' * 20, 'HTTP和requests库', '-' * 20)
import requests

print('-' * 20, '获取搜狐网首页', '-' * 20)

# requests的get函数会返回一个Response对象
resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    # 通过Response对象的text属性获取服务器返回的文本内容
    print(resp.text)
print('-' * 20, '获取百度Logo并保存', '-' * 20)
resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')

with open('image/baidu.png', 'wb') as file:
    # 通过Response对象的content属性获取服务器返回的二进制内容
    file.write(resp.content)
print('-' * 20, '开发爬虫/蜘蛛程序', '-' * 20)
import random
import re
import time

for page in range(1, 11):
    resp = requests.get(
        # 请求https://movie.douban.com/top250时，start参数代表了从哪一部电影开始
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出爬虫程序而阻止我们的请求
        # User-Agent可以设置为浏览器的标识（可以在浏览器的开发者工具查看HTTP请求头找到）
        # 由于豆瓣网允许百度爬虫获取它的数据，因此直接将我们的爬虫伪装成百度的爬虫
        headers={'User-Agent': 'BaiduSpider'}
    )
    # 创建正则表达式对象，通过捕获组捕获span标签中的电影标题
    pattern = re.compile(r'\<span class="title"\>([^&]*?)\</span\>')
    # 通过正则表达式获取class属性为title且标签内容不以&符号开头的span标签
    results = pattern.findall(resp.text)
    # 循环变量列表中所有的电影标题
    for result in results:
        print(result)
    # 随机休眠1-3秒，避免获取页面过于频繁
    time.sleep(random.randint(1, 3))
