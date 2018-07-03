#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/22 5:01 PM
# @Author  : playboy

import urllib
import urllib2
import re
import cookielib


# 登陆豆瓣
def login(capt):
    # 构建一个CookieJar对象
    cookie = cookielib.CookieJar()
    # 创建cookie处理器对象
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    # 构建opener
    opener = urllib2.build_opener(cookie_handler)

    url = "https://accounts.douban.com/login"
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}
    phone = raw_input("请输入账号:")
    password = raw_input("请输入密码:")
    code = raw_input("请输入验证码:")
    data = {
        "source": "index_nav",
        "redir": "https://www.douban.com",
        "form_email": phone,
        "form_password": password,
        "captcha-solution": code,
        "captcha-id": capt,
        "login": "登陆"
    }
    data = urllib.urlencode(data)
    request = urllib2.Request(url, data=data, headers=header)
    # 通过opener发送这个请求，并获取登录后的cookie值
    opener.open(request)
    # 访问需要cookie的页面
    response = opener.open("https://www.douban.com/people/138218720/")
    print(response.read())


# 处理验证码
def handle_code():
    url = "https://accounts.douban.com/login"
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}
    request = urllib2.Request(url, headers=header)
    html = urllib2.urlopen(request).read()

    # 正则处理
    pattern = re.compile('<img id="captcha_image" src="(.*?)" alt', re.S)
    img = pattern.findall(html)[0]
    print(img)
    write_image(img)


# 将图片写入本地
def write_image(img_url):
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"}
    request = urllib2.Request(img_url, headers=header)
    image = urllib2.urlopen(request).read()
    with open("code.jpg", "w") as f:
        f.write(image)

    # 获取captcha-id
    pattern = re.compile("id=(.*?)&")
    capt = pattern.findall(img_url)[0]
    login(capt)


handle_code()
