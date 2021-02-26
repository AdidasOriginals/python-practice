"""vote_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from polls.views import show_subjects, show_teachers
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index),
    path('subjects/', views.SubjectView.as_view()),
    path('teachers/', views.show_teachers),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login/', views.login),
    path('register/', views.register),
    path('captcha/', views.get_captcha),
    path('check/', views.check_unique),
    path('mobilecode/<str:tel>/', views.get_mobilecode),
    path('logout/', views.logout),
    path('report/', views.report),
    path('excel/', views.export_teachers_excel),
    path('pdf/', views.export_pdf),
    path('teachers_data/', views.get_teachers_data),
    path('bar/', views.get_bar_data),

]
