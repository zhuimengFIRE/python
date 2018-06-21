#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 4:35 PM
# @Author  : playboy

from threading import Thread,Lock

num = 0

def func1():
    global num
    for i in range(1000000):
        # True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这里一直等待到解锁为止
        # False表示非堵塞，即不管本次调用能够成功上锁，都不会卡在这,而是继续执行下面的代码
        flag = mutex.acquire(True)
        if flag:
            num += 1
            mutex.release()

    print('func1--num=%d'%num)

def func2():
    global num
    for i in range(1000000):
        flag = mutex.acquire(True)
        if flag:
            num += 1
            mutex.release()

    print('func2--num=%d' % num)


mutex = Lock()

p1 = Thread(target=func1)
p1.start()

p2 = Thread(target=func2)
p2.start()

print('num=%d'%num)