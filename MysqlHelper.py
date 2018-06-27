#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 4:04 PM
# @Author  : playboy

import pymysql


class MysqlHelper():
    def __init__(self, host, user_name, password, db_name):
        self.host = host
        self.user_name = user_name
        self.password = password
        self.db_name = db_name
        self.connect()

    # 连接数据库
    def connect(self):
        self.db = pymysql.connect(self.host, self.user_name, self.password, self.db_name)
        self.cursor = self.db.cursor()

    # 创建表
    def create_table(self, sql):
        self.cursor.execute(sql)

    # 插入数据
    def insert_data(self, sql):
        self.__edit(sql)

    # 修改数据
    def update_data(self, sql):
        self.__edit(sql)

    # 查询数据
    def find_data(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    # 删除数据
    def delete_data(self, sql):
        self.__edit(sql)

    # 执行sql语句
    def __edit(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    # 关闭数据库
    def close_data(self):
        self.db.close()

