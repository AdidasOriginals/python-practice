#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/8 10:56 
# @Author : Edison
# @Version：V 0.1
# @File : test-024.py
# @desc :对象的序列化和反序列化
import json

print('-' * 20, '读写JSON格式的数据', '-' * 20)
my_dict = {
    'name': 'DanielWu',
    'age': 18,
    'friends': ['吴彦祖的fans', '吴彦祖的fans2'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
# 中文是用Unicode编码书写的
print('字典已保存到data.json文件中')
with open('data.json', 'r') as file:
    my_dict_new = json.load(file)
    print(type(my_dict_new))
    print(my_dict_new)
print('-' * 20, '包管理工具pip的使用', '-' * 20)
# pip --version
# pip install ujson
# python.exe -m pip install --upgrade pip
# 在默认情况下，pip会访问https://pypi.org/simple/来获得三方库相关的数据，
# 但是国内访问这个网站的速度并不是十分理想，因此国内用户可以使用豆瓣网提供的镜像来替代这个默认的下载源
# pip install ujson -i https://pypi.doubanio.com/simple
# 可以通过pip search命令根据名字查找需要的三方库
# pip search ujson
# 可以通过pip list命令来查看已经安装过的三方库
# pip list
# 更新某个三方库，可以使用pip install -U或pip install --upgrade
# pip install -U
# pip install --upgrade
# pip install -U ujson -i https://pypi.doubanio.com/simple
# python -m pip install -U pip 更新pip系统本身 python -m pip install --upgrade pip --user
# 要删除某个三方库，可以使用pip uninstall命令
# pip uninstall
# pip uninstall -y ujson
print('-' * 20, '使用网络API获取数据', '-' * 20)
import requests
import json
import time
import pandas as pd
from pyecharts import options as opts
# from pyecharts.charts import Map
from pyecharts.charts import Bar, Pie, Grid
import matplotlib.pyplot as plt

# 获取国内新闻并显示新闻标题和链接。
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    # d = json.loads(resp.text)
    # print(d)
    # for item in data_model.items():
    #     print(item)
    data_model = resp.json()
    data = json.loads(data_model['data'])
    world = data['areaTree']
    print(world)
    world_df = pd.json_normalize(world)
    print(world_df)
    china = world_df.loc[world_df.name == '中国', 'children'].values[0]
    print(china)
    china_df = pd.json_normalize(china)
    print(china_df)
    # 提取各地市的数据，并合并成一个dataframe
    china_city = None  # 初始化一个变量
    for province in china_df.name:  # 按照每个省来循环
        city = china_df.loc[china_df.name == province, 'children'].values[0]  # 提取省内各地市的疫情数据
        city_df = pd.json_normalize(city)  # 将数据转化成dataframe格式
        city_df['province'] = province  # 增加一列作为省名
        china_city = city_df.append(china_city)  # 将数据添加到全国的汇总数据中
        # 选取关注的列并重新设置index
        china_city = china_city[[
            'province', 'name',
            'today.confirm', 'total.confirm', 'total.suspect',
            'total.dead', 'total.deadRate', 'total.healRate'
        ]].reset_index(drop=True)
    # print(china_city)
    chinaTotaldata = pd.DataFrame(china_city)
    df2 = china_city.sort_values(by=['total.confirm'], ascending=False)
    print(df2)
    pie = Pie()
    pie.add(
        "",
        [list(i) for i in zip(df2['province'].values.tolist(), df2['total.confirm'].values.tolist())],
        radius=["10%", "30%"]
    )
    pie.set_series_opts(label_opts = opts.LabelOpts(formatter="{b}:{c}"))
    pie.render()
