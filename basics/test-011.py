#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/20 15:59 
# @Author : Edison
# @Version：V 0.1
# @File : test-011.py
# @desc :文件和异常
print('读写文本文件'.center(50, '-'))


def main():
    f = open('data/python.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


main()


def main2():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


# main2()
def main3():
    try:
        with open('data/python.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


# main3()
# 除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
import time


def main4():
    # encoding='utf-8' 不加报错：
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 4: illegal multibyte sequence
    # 一次性读取整个文件内容
    with open('data/致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    print('-' * 88)
    # 通过for-in循环逐行读取
    with open('data/致橡树.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    print('-' * 88)

    # 读取文件按行读取到列表中
    with open('data/致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


# main4()
# 写文件
from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main5():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open('./data/' + filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')


# main5()
print('读写二进制文件'.center(50, '-'))


def main6():
    try:
        with open('image/dog.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('image/dog3.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


# main6()
print('读写JSON文件'.center(50, '-'))
import json


def main7():
    mydict = {
        'name': '吴彦祖',
        'age': '42',
        'qq': '88888',
        'friends': ['古天乐', '金城武', '谢霆锋'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data/test_data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')


main7()
print('访问网络API'.center(50, '-'))
import requests
import json


def main8():
    # APIKEY为自己申请的key
    url = 'http://api.tianapi.com/txapi/tianqi/index?key=APIKEY&city=北京市'
    resp = requests.get(url)
    data_model = json.loads(resp.text)
    weather_info = data_model['newslist']
    for weather in weather_info:
        print(weather)


main8()
# {'area': '北京', 'date': '2021-01-21', 'week': '星期四', 'weather': '晴', 'weatherimg': 'qing.png', 'real': '4℃', 'lowest': '-5℃', 'highest': '6℃', 'wind': '西南风', 'winddeg': '225', 'windspeed': '3', 'windsc': '1-2级', 'sunrise': '07:30', 'sunset': '17:22', 'moonrise': '11:53', 'moondown': '00:29', 'pcpn': '0.0', 'pop': '0', 'uv_index': '3', 'vis': '25', 'humidity': '45', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。晴天紫外线等级较高，外出注意补水防晒。'}
# {'area': '北京', 'date': '2021-01-22', 'week': '星期五', 'weather': '晴转多云', 'weatherimg': 'yun.png', 'real': '3℃', 'lowest': '-7℃', 'highest': '5℃', 'wind': '南风', 'winddeg': '180', 'windspeed': '3', 'windsc': '1-2级', 'sunrise': '07:29', 'sunset': '17:23', 'moonrise': '12:18', 'moondown': '01:28', 'pcpn': '0.0', 'pop': '0', 'uv_index': '3', 'vis': '25', 'humidity': '62', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。'}
# {'area': '北京', 'date': '2021-01-23', 'week': '星期六', 'weather': '多云', 'weatherimg': 'yun.png', 'real': '2℃', 'lowest': '-6℃', 'highest': '4℃', 'wind': '南风', 'winddeg': '180', 'windspeed': '3', 'windsc': '1-2级', 'sunrise': '07:29', 'sunset': '17:24', 'moonrise': '12:47', 'moondown': '02:27', 'pcpn': '0.0', 'pop': '1', 'uv_index': '3', 'vis': '25', 'humidity': '59', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。'}
# {'area': '北京', 'date': '2021-01-24', 'week': '星期日', 'weather': '晴转多云', 'weatherimg': 'yun.png', 'real': '5℃', 'lowest': '-4℃', 'highest': '7℃', 'wind': '东北风', 'winddeg': '45', 'windspeed': '3', 'windsc': '1-2级', 'sunrise': '07:28', 'sunset': '17:25', 'moonrise': '13:21', 'moondown': '03:28', 'pcpn': '0.0', 'pop': '0', 'uv_index': '3', 'vis': '15', 'humidity': '54', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。'}
# {'area': '北京', 'date': '2021-01-25', 'week': '星期一', 'weather': '小雪转多云', 'weatherimg': 'yun.png', 'real': '0℃', 'lowest': '-5℃', 'highest': '2℃', 'wind': '东南风', 'winddeg': '135', 'windspeed': '3', 'windsc': '1-2级', 'sunrise': '07:27', 'sunset': '17:26', 'moonrise': '14:01', 'moondown': '04:28', 'pcpn': '0.7', 'pop': '12', 'uv_index': '1', 'vis': '24', 'humidity': '43', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。'}
# {'area': '北京', 'date': '2021-01-26', 'week': '星期二', 'weather': '晴转多云', 'weatherimg': 'yun.png', 'real': '5℃', 'lowest': '-5℃', 'highest': '7℃', 'wind': '西南风', 'winddeg': '225', 'windspeed': '6', 'windsc': '1-2级', 'sunrise': '07:26', 'sunset': '17:28', 'moonrise': '14:48', 'moondown': '05:27', 'pcpn': '0.0', 'pop': '0', 'uv_index': '3', 'vis': '25', 'humidity': '31', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。'}
# {'area': '北京', 'date': '2021-01-27', 'week': '星期三', 'weather': '多云', 'weatherimg': 'yun.png', 'real': '3℃', 'lowest': '-5℃', 'highest': '5℃', 'wind': '东北风', 'winddeg': '45', 'windspeed': '6', 'windsc': '1-2级', 'sunrise': '07:25', 'sunset': '17:29', 'moonrise': '15:44', 'moondown': '06:22', 'pcpn': '0.0', 'pop': '1', 'uv_index': '3', 'vis': '25', 'humidity': '34', 'tips': '天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。'}
