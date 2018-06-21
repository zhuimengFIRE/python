#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 11:31 AM
# @Author  : playboy

from socket import *

udp = socket(AF_INET, SOCK_DGRAM)

# 绑定本地的相关信息
bindInfo = ('', 7781)

udp.bind(bindInfo)

sendAddr = ('10.211.55.4', 8080)

sendData = udp.sendto('test'.encode(),sendAddr)

recvData = udp.recvfrom(1024)

print(recvData)

udp.close()