#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 21:26
# @Author  : playboy

import re

pattern = re.compile("\d+")

# match表示从第一个开始匹配
m = pattern.match(r"12sadsa")

print(m.group())
print(m.span()) # 范围 起始位置和结束位置

# search从任意位置查找
m = pattern.search(r"aa123aa3")

print(m.group())
print(m.span())