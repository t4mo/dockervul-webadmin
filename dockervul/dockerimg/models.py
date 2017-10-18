# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dockervul.tools import DockerCommand

# Create your models here.
class Dockerimg(models.Model):
    imgname = models.CharField(max_length=50, blank=True)
    imgdid=models.CharField(max_length=255, blank=True)
    ports = models.CharField(max_length=255,blank=True)

