#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: For lg224@foxmail.com
# @Date  : 10/15/17



from django.conf.urls import url
from . import views

app_name = 'dockerimg'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^statr/(\w+)$', views.start, name='start'),
    url(r'^run/(\w+)$', views.run, name='run'),
]