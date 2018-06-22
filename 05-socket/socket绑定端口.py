#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 11:31 AM
# @Author  : playboy

# 导入socket模块
from socket import *

if __name__ == '__main__':

    # 创建一个udp套接字
    udp = socket(AF_INET, SOCK_DGRAM)

    # 绑定本地的相关信息 ip和端口
    bindInfo = ('', 7781)
    udp.bind(bindInfo)

    # 目的主机的ip和端口
    sendAddr = ('10.211.55.4', 8080)

    # 输入你要发送的内容
    send = input('你要发送的内容是：')

    # 发送给目的主机
    sendData = udp.sendto(send.encode(), sendAddr)

    # 接收目的主机发送的内容 1024表示接收的最大字节数
    recvData = udp.recvfrom(1024)

    # 打印接收到的数据
    print(recvData)

    # 关闭套接字
    udp.close()