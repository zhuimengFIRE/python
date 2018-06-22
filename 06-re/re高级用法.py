#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 4:38 PM
# @Author  : playboy

import re

# search
ret = re.search(r'\d+','h2hu:782')
print(ret.group())

# findall
ret1 = re.findall(r'\d+','aa=11,bb=22,cc=33')
print(ret1)

# sub 将匹配到的数据进行替换
ret2 = re.sub(r'\d+','11','aa=22')
print(ret2)

# split 根据匹配进行切割字符串，并返回一个列表
ret3 = re.split(r':| ','name:playboy age:25')
print(ret3)