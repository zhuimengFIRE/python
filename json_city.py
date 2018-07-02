#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 23:19
# @Author  : playboy

import urllib2
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/67.0.3396.99 Safari/537.36"}

request = urllib2.Request(url, headers=header)
response = urllib2.urlopen(request)
html = response.read()

# 把json字符串转换成python形式的Unicode字符串
unicodestr = json.loads(html)

city_list = jsonpath.jsonpath(unicodestr, "$..name")

for city in city_list:
    print(city)