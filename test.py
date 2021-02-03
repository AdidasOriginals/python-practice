# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/6 18:50
# @Author : Edison
# @Version：V 0.1
# @File : test.py
# @desc :
import requests
import json
import time
import pandas as pd


# 获取国内新闻并显示新闻标题和链接。
def getData():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return json.loads(resp.json()['data'])


if __name__ == '__main__':
    data_dict = getData()
    # 打印字典的key
    print(data_dict.keys())
    # 获取国内所有数据
    chinaAreadict = data_dict['areaTree'][0]
    provincelist = chinaAreadict['children']


def foo():
    print('test,goodbye, world!')
