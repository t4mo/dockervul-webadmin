#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py
# @Author: For lg224@foxmail.com
# @Date  : 10/15/17
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email",'phone')
        fields = ("username", "email",'phone')
        fields = ("username", "email",'phone')
        fields = ("username", "email",'phone')