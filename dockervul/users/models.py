# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ipsaddres = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone = models.IntegerField(blank=True)

    class Meta(AbstractUser.Meta):
        pass