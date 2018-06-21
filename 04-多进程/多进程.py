#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 上午9:20
# @Author  : playboy

import os

# windows上没有fork
pid = os.fork()

if pid == 0:
    print("--1--")
else:
    print("--2--")


