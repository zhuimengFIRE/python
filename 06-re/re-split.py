#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 21:47
# @Author  : playboy

import re

# 匹配空格\s 数字\d 斜杠\\\ 分号;
pattern = re.compile("[\s\d\\\;]+")

# 根据上面的正则切割
m = pattern.split(r"a bb\aa;m1m;     a")
print(m)


