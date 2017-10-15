#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DockerCommand.py
# @Author: For lg224@foxmail.com
# @Date  : 9/23/17

import docker
import json
import random




class DockerCommand:

    def __init__(self, url='127.0.0.1',port='2375', version='1.21'):
        self.url='tcp://'+url+':'+port
        self.client = docker.APIClient(base_url=self.url, version=version, timeout=10)

    #run img

    def run(self, imgid,ports):
        containerId = self.client.create_container(image=imgid, ports=ports,
                                                   host_config=self.client.create_host_config(port_bindings={
                                                       ports[0]:str(random.uniform(1, 10))[-4:],
                                                       ports[1]: str(random.uniform(1, 10))[-4:]
                                                   }),
                                                   stdin_open=True, tty=True, )
        try:
            self.client.start(container=containerId['Id'])
            return containerId['Id']
        except Exception,e:
            return False





a=DockerCommand()
print a.run('bda0bf833bab',[80,443])