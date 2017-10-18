#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DockerCommand.py
# @Author: For lg224@foxmail.com
# @Date  : 9/23/17

import docker
import json
import random
from dwebsocket import accept_websocket,require_websocket




class DockerCommand:

    def __init__(self, url='127.0.0.1',port='2375', version='1.21'):
        self.url='tcp://'+url+':'+port
        self.client = docker.APIClient(base_url=self.url, version=version, timeout=10)

    #run img

    def run(self, imgid,ports):
        datas=['8080',]
        if(ports.find(',')):
            datas.append(ports)

        containerId = self.client.create_container(image=imgid, ports=ports,
                                                   host_config=self.client.create_host_config(port_bindings={
                                                       datas[0]:str(random.uniform(1, 10))[-4:],
                                                       datas[1]: str(random.uniform(1, 10))[-4:]

                                                   }),
                                                   stdin_open=True, tty=True, )
        try:
            return containerId['Id']
        except Exception,e:
            return False



    @accept_websocket
    def getsocket(self,request,containerId):


        if request.is_websocket:
            request.websocket.send('Welcome to shell')
            try:
                container = self.client.exec_create(container=containerId, cmd="/bin/bash", user='root',tty=True,stdout=True,stderr=True,stdin=True,)
                a = self.client.exec_start(container['Id'], stream=True, tty=True, detach=False,socket=True)
                self.client.exec_resize(container['Id'], height=40, width=80)
                for message in request.websocket:
                    if not message:
                        break
                    a.send(message.encode('utf-8'))

                    request.websocket.send(a.recv(65535))
            except Exception,e:
                request.websocket.send('error')

