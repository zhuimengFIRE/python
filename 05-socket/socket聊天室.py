#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 2:02 PM
# @Author  : playboy

from socket import *
from time import ctime

# 创建套接字
udp = socket(AF_INET, SOCK_DGRAM)

server = ('10.211.55.4',8080)

# 绑定本地信息
bindAddr = ('',7878)
udp.bind(bindAddr)


udp.sendto('hello\n'.encode(), server)



while True:

    recvData = udp.recvfrom(1024)
    print('[%s] %s:%s'%(ctime(),recvData[1][0],recvData[0]))

    sendData = input('你要发送的是：')

    udp.sendto((sendData+'\n').encode(),server)


udp.close()