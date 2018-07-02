#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 19:27
# @Author  : playboy

import urllib
import urllib2
from lxml import etree


def loadPage(url):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/67.0.3396.99 Safari/537.36"}
    request = urllib2.Request(url, headers=header)
    respone = urllib2.urlopen(request)
    html = respone.read()

    # 解析html文档
    content = etree.HTML(html)
    print(content)
    # 返回所有匹配后的列表集合
    link_list = content.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    for link in link_list:
        fulllink = "http://tieba.baidu.com"+link
        print(fulllink)
        # loadImage(fulllink)


# 取出每个帖子里面的图片链接
def loadImage(link):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/67.0.3396.99 Safari/537.36"}
    request = urllib2.Request(link, headers=header)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html)

    # 返回帖子里所有有图片的列表集合
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        fulllink = "http://tieba.baidu.com"+link
        writeImage(fulllink)


def writeImage(link):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/67.0.3396.99 Safari/537.36"}
    request = urllib2.Request(link,headers=header)
    image = urllib2.urlopen(request).read()
    filename = link[-10:]
    with open("/Users/playboy/Desktop/heima/image/"+filename,'w') as f:
        f.write(image)
    print("已成功下载图片" + filename)


def tiebaSpaider(name, beginPage, endPage):
    url = "http://tieba.baidu.com/f?"
    kw = urllib.urlencode({"kw":name})
    for i in range(beginPage, endPage+1):
        fullUrl = url + kw + '&pn=' + str((i - 1) * 50)
        print(fullUrl)
        loadPage(fullUrl)
    print("谢谢使用")


if __name__ == '__main__':
    name = raw_input("请输入贴吧名称：")
    beginPage = int(raw_input("请输入开始页码："))
    endPage = int(raw_input("请输入结束页码:"))
    tiebaSpaider(name, beginPage, endPage)

