#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 4:10 PM
# @Author  : playboy

from threading import Thread
import time

num = 100

def func1():
    global num
    num += 1
    print('func1---%d'%num)

def func2():
    global num
    print('func2---%d'%num)


t1 = Thread(target=func1)
t1.start()

# 延时保证t1线程中的事情做完
time.sleep(1)

t2 = Thread(target=func2)
t2.start()

