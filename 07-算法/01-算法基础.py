#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 10:33
# @Author  : playboy

import time

# 算法五大特效 输入 输出 有穷性 确定性 可行性

# a+b+c = 1000,a*a + b*b = c*c 求出abc的所有可能性

# 枚举法

start_time = time.time()

# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a+b+c == 1000 & a*a + b*b == c*c:
#                 print(a, b, c)

# T(n) = O(n3)  时间复杂度为n的三次方


for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if a*a + b*b == c*c:
            print(a, b, c)

# T(n) = O(n2)

end_time = time.time()
print('times=%d' % (end_time-start_time))
print('end')
