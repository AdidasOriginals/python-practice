from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Subject, Teacher


class SubjectModelAdmin(admin.ModelAdmin):
    # 和数据库字段名称对应
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'gcount', 'bcount', 'subject')
    search_fields = ('name',)
    ordering = ('no',)


admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Teacher, TeacherModelAdmin)
