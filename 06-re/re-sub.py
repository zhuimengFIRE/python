#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 21:56
# @Author  : playboy

import re

pattern = re.compile("(\w+) (\w+)")
s = "hello 123, hello 456"
m = pattern.sub(r"playboy", s)
print(m)

# 把所有数字替换成xxx
pattern1 = re.compile("\d+")
s = "aaa123bbb456"
m = pattern1.sub(r"xxx", s)
print(m)
