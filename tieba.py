#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 19:27
# @Author  : playboy

import urllib
import urllib2

def loadPage(url):
    header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    request = urllib2.Request(url,headers=header)
    respone = urllib2.urlopen(request)
    return respone.read()


def writeFile(html,fileName):
    with open('/Users/playboy/Desktop/heima/tieba/'+fileName, 'w') as f:
        f.write(html)


def tiebaSpaider(name, beginPage, endPage):
    url = "http://tieba.baidu.com/f?"
    kw = urllib.urlencode({"kw":name})
    for i in range(beginPage, endPage+1):
        fullUrl = url + kw + '&pn=' + str((i - 1) * 50)
        print("正在下载第%d页"%i)
        html = loadPage(fullUrl)
        print("正在保存第%d页"%i)
        writeFile(html,name+'吧第'+str(i)+'页')
    print("谢谢使用")


if __name__ == '__main__':
    name = raw_input("请输入贴吧名称：")
    beginPage = int(raw_input("请输入开始页码："))
    endPage = int(raw_input("请输入结束页码:"))
    tiebaSpaider(name, beginPage, endPage)

