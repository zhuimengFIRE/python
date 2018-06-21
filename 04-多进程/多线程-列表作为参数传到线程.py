#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 4:17 PM
# @Author  : playboy

from threading import Thread
import time

def func1(nums):
    nums.append(444)
    print('func1--%s'%nums)

def func2(nums):
    print('func2--%s'%nums)


num = [111,222,333]

# 开启线程并传递参数
t1 = Thread(target=func1,args=(num,))
t1.start()

# 保证t1执行完毕
time.sleep(1)

t2 = Thread(target=func2,args=(num,))
t2.start()