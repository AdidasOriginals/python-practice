"""
Django settings for vote_django project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^__&vii3lpws^$zyv&dbun^_wi8bo)^25wq$6crqkrqhb2$23s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'rest_framework',
]

REST_FRAMEWORK = {
    'PAGE_SIZE': 2,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vote_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vote_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'django.db.backends.sqlite3'：SQLite嵌入式数据库。
        # 'django.db.backends.postgresql'：BSD许可证下发行的开源关系型数据库产品。
        # 'django.db.backends.mysql'：甲骨文公司经济高效的数据库产品。
        # 'django.db.backends.oracle'：甲骨文公司关系型数据库旗舰产品。
        # 数据库引擎配置
        'ENGINE': 'django.db.backends.mysql',
        # 数据库的名字
        'NAME': 'vote',
        # 数据库服务器的IP地址（本机可以写localhost或127.0.0.1）
        'HOST': 'localhost',
        # 启动MySQL服务的端口号
        'PORT': 3306,
        # 数据库用户名和口令
        'USER': 'vote',
        'PASSWORD': 'yourPassword',
        # 数据库使用的字符集
        'CHARSET': 'utf8mb4',
        # 数据库时间日期的时区设定
        'TIME_ZONE': 'Asia/Chongqing',
    }
}

# 缓存配置
CACHES = {
    'default': {
        # 指定通过django-redis接入Redis服务
        'BACKEND': 'django_redis.cache.RedisCache',
        # Redis服务器的URL
        'LOCATION': [
            'redis://127.0.0.1:6379/0',
        ],
        # Redis中键的前缀（解决命名冲突问题）
        'KEY_PREFIX': 'vote',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # 连接池（预置若干备用的Redis连接）配置
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 512,
            },
            # 连接Redis认证用户身份的口令
            'PASSWORD': 'yourPassword',
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# 默认语言修改为中文
LANGUAGE_CODE = 'zh-hans'

# 时区设置为东八区
TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# 显示静态资源图片
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_URL = '/static/'