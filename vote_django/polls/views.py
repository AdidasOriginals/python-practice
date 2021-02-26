from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from polls.models import Subject, Teacher, User
from polls.utils import gen_random_code, check_username, check_password, check_tel, \
    gen_sha256_digest, gen_md5_digest, random_code, LoginRequiredAuthentication
from polls.captcha import Captcha
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
import jwt
from django.conf import settings
from django_redis import get_redis_connection
from django.db import DatabaseError
from rest_framework.generics import ListAPIView
from polls.serializers import SubjectSerializer, TeacherSerializer, SubjectSimpleSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from jwt import InvalidTokenError


def show_subjects(request):
    """显示学科"""
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})
    # result = serializers.serialize("json", Subject.objects.all())
    # return JsonResponse(result, safe=False)


class SubjectView(ListAPIView):
    # 指定如何获取数据
    queryset = Subject.objects.all()
    # 指定如何序列化数据
    serializer_class = SubjectSerializer
    # 指定如何验证用户身份
    # authentication_classes = [LoginRequiredAuthentication, ]


def show_index(request):
    return redirect('/static/html/subjects.html')


@api_view(('GET',))
@authentication_classes([LoginRequiredAuthentication, ])
def show_teachers(request):
    """获取老师数据"""
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.only('name').get(no=sno)
        queryset = Teacher.objects.defer('subject').filter(subject=sno)
        serializer = TeacherSerializer(queryset, many=True)
        data = {
            'code': 20000,
            'subject': {'no': subject.no, 'name': subject.name},
            'teachers': serializer.data
        }
    except (KeyError, ValueError, Subject.DoesNotExist) as err:
        data = {'code': 20001, 'message': '获取学科老师数据失败'}
    return Response(data)


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    """好评"""
    token = request.META.get('HTTP_TOKEN')
    print(token)
    if token:
        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise'):
                teacher.gcount += 1
                count = teacher.gcount
            else:
                teacher.bcount += 1
                count = teacher.bcount
            teacher.save()
            data = {'code': 20000, 'msg': '投票成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'msg': '投票失败'}
        except InvalidTokenError:
            data = {'code': 20002, 'mesg': '登录已过期，请重新登录'}
    else:
        data = {'code': 20002, 'mesg': '请先登录'}
    return JsonResponse(data)


@api_view(('POST',))
def login(request: HttpRequest) -> HttpResponse:
    """登录"""
    hint = request.GET.get('hint') or ''
    if request.method == 'POST':
        username = request.data.get('username', '').strip()
        password = request.data.get('password', '')
        if check_username(username) and check_password(password):
            password = gen_sha256_digest(password)
            user = User.objects.filter(Q(username=username) | Q(tel=username)) \
                .filter(password=password).first()
            if user:
                user.last_visit = timezone.now()
                user.save()
                payload = {
                    'userid': user.no,
                    'exp': timezone.now() + timedelta(days=1)
                }
                # 通过PyJWT的encode函数生成用户身份令牌（bytes，可以通过decode方法处理成str）
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
                return Response({'code': 40000, 'hint': '登录成功', 'token': token, 'username': user.username})
            else:
                hint = '登录失败，用户名或密码错误'
        else:
            hint = '请输入有效的登录信息'
    return Response({'code': 40001, 'hint': hint})


@api_view(('POST',))
def register(request):
    """用户注册"""
    username, tel, hint = '', '', ''
    if request.method == 'POST':
        agreement = request.data.get('agreement')
        if agreement:
            username = request.data.get('username', '').strip()
            password = request.data.get('password', '')
            tel = request.data.get('tel', '').strip()
            redis_cli = get_redis_connection()
            code_from_user = request.data.get('mobilecode', '0')
            code_from_redis = redis_cli.get(f'mobile:valid:{tel}').decode()
            if code_from_user == code_from_redis:
                if check_username(username) and check_password(password) and check_tel(tel):
                    password = gen_sha256_digest(password)
                    try:
                        user = User(username=username, password=password, tel=tel)
                        user.last_visit = timezone.now()
                        user.save()
                        # 验证码只能消费一次，注册成功用过的验证码立即失效
                        redis_cli.delete(f'mobile:valid:{tel}')
                        hint = '注册成功，请登录'
                        # return redirect(f'/login/?hint={hint}')
                        return Response({'code': 30000, 'mesg': hint})
                    except DatabaseError:
                        hint = '注册失败，用户名或手机号已被使用'
                else:
                    hint = '请输入有效的注册信息'
            else:
                hint = '请输入正确的手机验证码'
        else:
            hint = '请勾选同意网站用户协议及隐私政策'
    # return render(request, 'register.html', {'hint': hint, 'username': username, 'tel': tel})
    return Response({'code': 30001, 'mesg': hint})


def logout(request):
    """注销（退出登录）"""
    request.session.flush()
    resp = redirect('/')
    resp.delete_cookie('username')
    return resp


def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    print(captcha_text)
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def check_unique(request):
    flag = False
    username = request.GET.get('username', '').strip()
    if check_username(username):
        user = User.objects.filter(username=username).first()
        flag = user is None
    return JsonResponse({'is_valid': flag})


def get_mobilecode(request, tel):
    """获取短信验证码"""
    if check_tel(tel):
        redis_cli = get_redis_connection()
        if redis_cli.exists(f'mobile:block:{tel}'):
            data = {'code': 30002, 'message': '请不要在60秒内重复发送短信验证码'}
        else:
            code = random_code()
            # 将验证码在Redis中保留1分钟（有效期）
            redis_cli.set(f'mobile:valid:{tel}', code, ex=60)
            data = {'code': 30000, 'data': code, 'message': '短信验证码已发送，请注意查收'}
    else:
        data = {'code': 30001, 'message': '请输入有效的手机号'}
    return JsonResponse(data)
