#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 5:01 PM
# @Author  : playboy

import re

# 找出user@test.com
string = 'user<user@test.com>'
ret = re.search('<(.+)>', string)
ret1 = re.findall(r'<([^>]+)', string)
print(ret.group(1))
print(ret1[0])

# 1. 匹配网址
# 有一批网址：
#
# http://www.interoem.com/messageinfo.asp?id=35
# http://3995503.com/class/class09/news_show.asp?id=14
# http://lib.wzmc.edu.cn/news/onews.asp?id=769
# http://www.zy-ls.com/alfx.asp?newsid=377&id=6
# http://www.fincm.com/newslist.asp?id=415
# 需要 正则后为：
#
# http://www.interoem.com/
# http://3995503.com/
# http://lib.wzmc.edu.cn/
# http://www.zy-ls.com/
# http://www.fincm.com/


def test(url):
    return re.sub(r'(http://.+?/).*', lambda x: x.group(1), url)


ret = test('http://www.interoem.com/messageinfo.asp?id=35')
print(ret)

# 2. 找出单词
# 有一句英文如下：
#
# hello world ha ha
#
# 查找所有的单词


word = re.split(r' +', 'hello  world ha ha')
print(word)
