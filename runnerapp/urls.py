from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    path('uploadPlan', views.uploadPlan, name='上传训练计划'),
    path('getPlan', views.getPlan, name='查看某用户的所有相关的训练计划'),
    path('joinPlan', views.joinPlan, name='参与该项训练'),
    path('getJoinUsers', views.getJoinUsers, name='获取参与训练的所有用户'),
    path('getTable', views.getTable, name='获取赛事'),


]