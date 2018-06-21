#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 2:03 PM
# @Author  : playboy

from multiprocessing import Pool
import os

def test(num):
    print('---pid=%d---%d---'%(os.getpid(),num))


pool = Pool(3)

for i in range(10):

    pool.apply_async(test,(i,))

print('start')

# 关闭Pool，使其不再接受新的任务
pool.close()
# 主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用
# 如果这个地方没join，会导致进程池中的任务不会执行
pool.join()

print('end')