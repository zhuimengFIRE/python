#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 3:05 PM
# @Author  : playboy

import re

# .  匹配任意1个字符（除了\n）
# [] 匹配[]中列表的字符
# \d 匹配数字 0-9
# \D 匹配非数字
# \s 匹配空格
# \S 匹配非空白
# \w 匹配单词字符 即a-zA-Z0-9
# \W 匹配非单词字符

# 匹配以hello开头的字符串
res = re.match('hello','hello world')

res1 = re.match('[0-9]','122h3ello world')

# 第一个字符大写，后面小写
res2 = re.match('[A-z][a-z]*','Mm23kk')

# 匹配变量名是否有效
res3 = re.match('[a-zA-Z_]+[\w]*','name')

# 匹配出0-99的数字
res4 = re.match('[1-9]?[0-9]','9')

# 匹配8-20位的密码，可以是大小些字母、数字、下划线
res5 = re.match('[a-zA-Z0-9_]{8,20}','34dfasdfa21347au_aiuue2390')

# 匹配出163的邮箱地址，@之前有4-20位  $用来表示结尾
res6 = re.match('[a-zA-z0-9]{4,20}@163.com$','wenlistudent@163.com')

print(res.group())
print(res1.group())
print(res2.group())
print(res3.group())
print(res4.group())
print(res5.group())
print(res6.group())