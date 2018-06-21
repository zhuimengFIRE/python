#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 11:06 AM
# @Author  : playboy

from socket import *

# 1. 创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

# 2. 准备接收方的地址
sendAddr = ('10.211.55.4', 8080)

# 3. 从键盘获取数据
sendData = input("请输入要发送的数据:")

# 4. 发送数据到指定的电脑上
udpSocket.sendto(sendData.encode(), sendAddr)

# 5.等待接收对方发送的数据 1024表示接收最大字节数
recvData = udpSocket.recvfrom(1024)

# 6.显示接收数据
print(recvData)

# 7. 关闭套接字
udpSocket.close()