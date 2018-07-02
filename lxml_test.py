#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 5:01 PM
# @Author  : playboy


import urllib2
from lxml import etree


def test():
    url = "https://movie.douban.com/chart"
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/67.0.3396.99 Safari/537.36"}
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    content = etree.HTML(response.read())
    print content

    # 如果返回为空，有可能是有tbody 去掉就可以了
    span_list = content.xpath('//div[@class="indent"]/div/table/tr/td/div/a[@class]/span')
    for name in span_list:
        print name.text

    link_list = content.xpath('//div[@class="indent"]/div/table/tr/td/div/a/@href')
    for link in link_list:
        print link


test()
