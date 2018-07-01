#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 21:35
# @Author  : playboy

import re

# +表示匹配1次或无限次
pattern = re.compile("\d+")
m = pattern.findall(r"hello 1234 567 99")
print(m)

# ?表示匹配0次或1次
pattern1 = re.compile("\d?")
m1 = pattern1.findall(r"hello 1234 567 99")
print(m1)

# 从1到10之间匹配
m2 = pattern.findall(r"aaa123bbb456", 1, 10)
print(m2)

# finditer返回的是迭代器
m3 = pattern.finditer(r"aaa123bbb456")
for i in m3:
    print(i.group())
