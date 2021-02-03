#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/1 15:36 
# @Author : Edison
# @Version：V 0.1
# @File : test-034.py
# @desc :网络编程入门和网络应用开发
print('requests库'.center(50, '-'))
from time import time
from threading import Thread
import requests


# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('./image/download/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    requestUrl = 'http://api.tianapi.com/meinv/?key=APIKEY&num=10'
    resp = requests.get(requestUrl)
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现突破下载
        DownloadHanlder(url).start()


# main()
print('提供时间日期的服务器'.center(50, '-'))
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main2():
    # 1.创建套接字对象并制定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口（端口用于区分不通的服务）
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('localhost', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理（提供服务）
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址（由IP和端口两部分构成）
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()


# if __name__ == '__main__':
#     main2()
print('使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片'.center(50, '-'))
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main3():
    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'dog.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送json字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口（区分不同的服务）
    server.bind(('localhost', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('image/dog.jpg', 'rb') as f:
        # 将二进制数据处理成base64再编码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


# if __name__ == '__main__':
#     main3()
print('发送电子邮件'.center(50, '-'))
from smtplib import SMTP
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText


def main4():
    # 邮件发送账号
    from_addr = '@qq.com'
    # 接收邮件账号
    to_addrs = ['@qq.com']
    # 授权码
    qqCode = ''
    # 固定写死smtp服务器
    smtp_server = 'smtp.qq.com'
    # 固定端口
    smtp_port = 465
    # 配置服务器
    stmp = SMTP_SSL(smtp_server, smtp_port)
    # 登录密码
    stmp.login(from_addr, qqCode)
    message = MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')
    message['From'] = Header('吴彦祖', 'utf-8')
    message['To'] = Header('彭于晏', 'utf-8')
    message['Subject'] = Header('Hello', 'utf-8')
    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        print('邮件发送失败--' + str(e))
    print('邮件发送成功')


# main4()
print('发送电子邮件-附件'.center(50, '-'))
from smtplib import SMTP
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib


def main5():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    # 创建文本内容
    # text_content = MIMEText('附件中是一只可爱的狗子', 'plain', 'utf-8')
    # # 将文本内容添加到邮件消息对象中
    # message.attach(text_content)
    # 图片html+文本
    image_msg = """
           <html><body>
           <p>下面是一只可爱的狗子</p>
           <p>图片演示：</p><p><img src="cid:imageid" alt="imageid"></p>
           </body></html>
           """
    mail_image_msg = MIMEText(image_msg, 'html', 'utf-8')
    message.attach(mail_image_msg)
    message['From'] = Header('吴彦祖', 'utf-8')
    message['To'] = Header('彭于晏', 'utf-8')
    message['Subject'] = Header('文件+excel+图片', 'utf-8')
    # 读取文件并将文件作为附件添加到邮件消息对象中
    # 文本
    with open('data/dog.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=dog.txt'
        message.attach(txt)
    # Excel
    with open('data/test3.xlsx', 'rb') as f:
        xlsx = MIMEText(f.read(), 'base64', 'utf-8')
        xlsx['Content-Type'] = 'application/vnd.ms-excel'
        xlsx['Content-Disposition'] = 'attachment; filename=student.xlsx'
        message.attach(xlsx)
    # 邮件正文图片-指定图片目录
    with open('image/dog.jpg', 'rb') as f:
        img_data = f.read()
        img = MIMEImage(img_data)
        # 定义图片 ID，在 HTML 文本中引用
        img.add_header('Content-ID', 'imageid')
        message.attach(img)
    # 图片附件
    with open('image/dog2.jpg', 'rb') as f:
        img_data = f.read()
        img = MIMEImage(img_data)
        # 定义图片 ID，在 HTML 文本中引用
        img.add_header('Content-Disposition', 'attachment', filename='dog2.jpg')
        message.attach(img)
    # 邮件发送账号
    from_addr = '@qq.com'
    # 接收邮件账号
    to_addrs = ['@qq.com']
    # 授权码
    qqCode = ''
    # 固定写死smtp服务器
    smtp_server = 'smtp.qq.com'
    # 固定端口
    smtp_port = 465
    # 配置服务器
    stmp = SMTP_SSL(smtp_server, smtp_port)
    # 登录密码
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    stmp.login(from_addr, qqCode)
    # 发送邮件
    stmp.sendmail(from_addr, to_addrs, message.as_string())
    # 与邮件服务器断开连接
    stmp.quit()
    print('邮件发送完成!')


# main5()
print('发送短信'.center(50, '-'))
import urllib.parse
import http.client
import json


def main6():
    host = '106.ihuyi.com'
    sms_send_url = '/webservices/sms.php?method=Submit'
    # 下面的参数需要填入自己注册的账号的对应的密码
    params = urllib.parse.urlencode(
        {'account': '账号', 'password': '密码', 'content': '您的验证码是:888888', 'mobile': '接收者的手机号', 'format': 'json'}
    )
    print(params)
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


main6()
