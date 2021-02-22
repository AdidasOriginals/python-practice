#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/22 11:00 
# @Author : Edison 
# @Version：V 0.1
# @File : basic_redis.py
# @desc : 在Python程序中使用Redis
import redis

client = redis.Redis(host='127.0.0.1', port=6379, password='yourpassword')
client.set('username', 'admin')
client.hset('student', 'name', 'DanielWu')
client.hset('student', 'age', 47)
print(client.keys('*'))
print(client.get('username'))
print(client.hgetall('student'))
