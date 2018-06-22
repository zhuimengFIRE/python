#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 10:12 AM
# @Author  : playboy

from multiprocessing import Queue

q = Queue(3)
q.put(111)
q.put(222)
q.put(333)

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())