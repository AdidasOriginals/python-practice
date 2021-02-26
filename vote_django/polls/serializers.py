"""
序列化：模型对象 ----> 字典 ----> JSON
通过继承DRF的ModelSerializer类自定义序列器实现模型对象的序列化
"""
from rest_framework.serializers import ModelSerializer

from polls.models import Subject, Teacher


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('subject',)


class SubjectSimpleSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('no', 'name')
