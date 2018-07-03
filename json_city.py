#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 23:19
# @Author  : playboy

import urllib2
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}

request = urllib2.Request(url, headers=header)
response = urllib2.urlopen(request)
html = response.read()

# 把json字符串转换成python形式的Unicode字符串
unicodestr = json.loads(html)

city_list = jsonpath.jsonpath(unicodestr, "$..name")

for city in city_list:
    print(city)

