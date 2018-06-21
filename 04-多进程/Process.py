#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 下午4:17
# @Author  : playboy

from multiprocessing import Process
import os

def run_proc(name):
    print('子进程运行中,name=%s,pid=%d' % (name,os.getpid()))

if __name__ == '__main__':
    print('父进程 %d' % os.getpid())

    # 创建子线程 并传递参数
    p = Process(target=run_proc, args=('test',))

    print('子进程将要运行')

    # 启动进程
    p.start()

    # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    # 或者可以设置等待多少秒
    p.join()

    print('子进程运行结束')