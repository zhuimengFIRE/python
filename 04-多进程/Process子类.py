#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 下午4:31
# @Author  : playboy

from multiprocessing import Process
import time

class MyProcess(Process):

    # 重写Process的run方法
    def run(self):
        while True:
            print('---test---')
            time.sleep(1)

if __name__ == '__main__':
    p = MyProcess()
    p.start()

    while True:
        print('---main---')
        time.sleep(1)
