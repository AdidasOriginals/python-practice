#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/24 14:54 
# @Author : Edison 
# @Version：V 0.1
# @File : utils.py
# @desc : 工具
import hashlib
import random
import re
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from polls.models import User
import jwt
from django.conf import settings
from jwt import InvalidTokenError

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

USERNAME_PATTERN = re.compile(r'\w{4,20}')
TEL_PATTERN = re.compile(r'1[3-9]\d{9}')


def gen_md5_digest(content):
    """将字符串处理成MD5摘要"""
    return hashlib.md5(content.encode()).hexdigest()


def gen_sha256_digest(content):
    """生成SHA256哈希摘要（签名、指纹）"""
    if not isinstance(content, bytes):
        if isinstance(content, str):
            content = content.encode('utf-8')
        else:
            content = bytes(content)
    return hashlib.sha256(content).hexdigest()


def gen_random_code(length=4):
    """生成指定长度的随机验证码"""
    return ''.join(random.choices(ALL_CHARS, k=length))


def check_username(username):
    """检查用户名"""
    return USERNAME_PATTERN.fullmatch(username) is not None


def check_password(password):
    """检查用户口令"""
    return len(password) >= 4


def check_tel(tel):
    """检查手机号"""
    return TEL_PATTERN.fullmatch(tel) is not None


def random_code(length=6):
    """生成随机短信验证码"""
    return ''.join(random.choices('0123456789', k=length))


# 里氏替换原则（Liskov Substitution Principle）
class LoginRequiredAuthentication(BaseAuthentication):
    """自定义认证类"""

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User()
            user.no = payload['userid']
            user.is_authenticated = True
            return user, token
        except InvalidTokenError:
            raise AuthenticationFailed('请提供有效的身份令牌')
