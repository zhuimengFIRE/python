#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 2:37 PM
# @Author  : playboy



import threading
import time

def test():
    print('test')
    time.sleep(1)

# 单线程
for i in range(3):
    test()


# 多线程
# 主线程会等待所有子线程结束后再结束
for i in range(10):
    t = threading.Thread(target=test)
    t.start()



class MyThread(threading.Thread):

    # 重写run方法
    def run(self):
        for x in range(3):
            print('run--%d--%s'%(x,self.name))
            time.sleep(1)


t = MyThread()
t.start()
