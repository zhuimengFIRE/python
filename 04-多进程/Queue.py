#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 2:14 PM
# @Author  : playboy


from multiprocessing import Queue


q = Queue(3)
q.put(111)
q.put(222)
q.put(333)

print(q.empty())

if not q.full():
    q.put_nowait(444)

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
