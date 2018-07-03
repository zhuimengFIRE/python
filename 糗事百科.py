#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 22:11
# @Author  : playboy

import urllib2
import re

class Spider:
    def __init__(self):
        self.page = 1
        self.switch = True


    # 下载页面
    def loadPage(self):
        print("正在下载数据...")
        url = "http://www.qiushibaike.com/8hr/page/"+str(self.page)+"/"
        header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}
        request = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(request)
        html = response.read()

        # 创建正则表达式规则对象 re.S表示全文匹配
        pattern = re.compile('<div class="content">(.*?)</div>', re.S)
        content_list = pattern.findall(html)

        # 处理拿到的结果
        self.dealContent(content_list)


    # 处理数据
    def dealContent(self, contents):
        print("正在写入数据...")
        for item in contents:
            item = item.replace("<span>", "").replace("</span>", "").replace("<br/>", "")
            self.writeFile(item)


    # 写入文件
    def writeFile(self, item):
        with open("/Users/playboy/Desktop/ziyuan/qiushi.txt", "a") as f:
            f.write(item)


    # 控制运行
    def startwork(self):
        while self.switch:
            self.loadPage()
            commend = raw_input("如果继续爬取，请按回车（退出输入quit）：")
            if commend == "quit":
                self.switch = False
            self.page += 1
        print("谢谢使用")


if __name__ == '__main__':
    spider = Spider()
    spider.startwork()