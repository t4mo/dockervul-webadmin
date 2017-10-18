# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Dockerimg
from django.contrib.auth.decorators import login_required


from dockervul.tools import DockerCommand
from django.http import HttpResponse

# Create your views here.
@login_required()
def index(request):
    imglist=Dockerimg.objects.all()
    return render(request,'admin/vul/index.html',{'imglist':imglist})

@login_required()
def statr(request,imgid):
    result = Dockerimg.objects.get(id=int(imgid))
    clent=DockerCommand()
    containerId=[]
    containerId['Id']=clent.run(result.imgdid,result.ports)
    return render(request, 'admin/vul/websocket.html', {'containerId': containerId['Id']})

@login_required()
def getCommod(request,tnerid):
    clent=DockerCommand()
    clent.getsocket(request,tnerid)

