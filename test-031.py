#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/14 19:19 
# @Author : Edison
# @Version：V 0.1
# @File : test-031.py
# @desc :用Python解析HTML页面
print('-' * 20, 'XPath解析', '-' * 20)
import random
import time
from lxml import etree
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'BaiduSpider',
        }
    )
    tree = etree.HTML(resp.text)
    # 通过XPath语法从页面中提取需要的数据
    spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
    for span in spans:
        print(span.text)
    time.sleep(random.randint(1, 3))
print('-' * 20, 'CSS选择器解析', '-' * 20)
import bs4

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'BaiduSpider',
        }
    )
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    # 通过CSS选择器从页面中提取需要的数据
    spans = soup.select('div.info>div.hd>a>span:nth-child(1)')
    for span in spans:
        print(span.text)
    time.sleep(random.randint(1, 3))
