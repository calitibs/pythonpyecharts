#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Administrator
@file: urls.py
@time: 2020/03/{DAY}
"""

from django.urls import path, re_path
from . import views


# urlpatterns = [
#     path('demo/', views.demo, name='demo'),
#     path('index/', views.index, name='index'),
#     path('word_cloud/', views.word_cloud, name='word_cloud'),
#     path('map/', views.heat_map, name='map'),
#     path('cure_line/', views.cure_line, name='cure_line'),
#     path('confirm_line/', views.confirm_line, name='confirm_line'),
#
# ]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='demo'),
    url(r'^word_cloud/$', views.word_cloud, name='word_cloud'),
    url(r'^map/$', views.heat_map, name='map'),
    url(r'^cure_line/$', views.cure_line, name='cure_line'),
    url(r'^confirm_line/$', views.confirm_line, name='confirm_line'),
]