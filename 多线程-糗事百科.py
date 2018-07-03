#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 23:14
# @Author  : playboy

import threading
from Queue import Queue
from lxml import etree
import requests
import json


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # 调用父类初始化方法
        super(ThreadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}

    def run(self):
        print("启动"+self.threadName)
        while not CRAWL_EXIT:
            try:
                # 取出一个数字 get里有个可选参数block 默认为true
                # 如果队列为空，block为true，不会结束，会进入阻塞状态，直到队列有新的数据
                # 如果队列为空，block为false，Queue.empty的异常
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                contents = requests.get(url, heders=self.headers)
                self.dataQueue.put(contents)
            except:
                pass
        print("结束"+self.threadName)


class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,filename,lock):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename
        self.lock = lock

    def run(self):
        print("启动"+self.threadName)
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
        print("退出"+self.threadName)

    def parse(self, html):
        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username": username,
                "image": image,
                "content": content,
                "zan": zan,
                "comments": comments
            }

            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
            with self.lock:
                # 写入存储的解析后的数据
                self.filename.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")



CRAWL_EXIT = False
PARSE_EXIT = False


def main():
    # 页码的队列，表示10个页面
    pageQueue = Queue(10)
    # 放入1-10的数字，先进先出
    for i in range(1,11):
        pageQueue.put(i)
    # 采集结果（每页html源码）的数据队列，参数为空不限制
    dataQueue = Queue()

    filename = open("duanzi.json", "a")

    # 创建锁
    lock = threading.Lock()

    # 三个采集线程的名字
    crawlList = ["采集线程1号","采集线程2号","采集线程3号"]

    # 存储三个采集线程
    threadcarwl = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcarwl.append(thread)

    parseList = ["解析线程1号","解析线程2号","解析线程3号"]
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue,filename,lock)
        thread.start()
        threadparse.append(thread)

    # 等待pageQueue队列为空
    while not pageQueue.empty():
        pass
    # 如果pageQueue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True

    print("pageQueue为空")

    for thread in threadcarwl:
        thread.join()
        print("1")

    while not dataQueue.empty():
        pass

    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in threadparse:
        thread.join()
        print "2"

    with lock:
        # 关闭文件
        filename.close()
    print "谢谢使用！"


if __name__ == '__main__':
    main()