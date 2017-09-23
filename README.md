# dockervul-webadmin
os
```
Kernel \r on an \m
```
start docker api

```
vim /etc/sysconfig/docker


add  OPTIONS='-H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock --selinux-enabled'

service docker restart

netstat -an|grep 2375
tcp        0      0 127.0.0.1:2375          0.0.0.0:*               LISTEN
```