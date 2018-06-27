#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 9:35 AM
# @Author  : playboy


import pymysql

# 打开数据库连接
db = pymysql.connect('10.211.55.3', 'root', 'chaoer1314', 'student')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute('drop table if exists test')

# 新建表
sql_table = "create table if not exists test(name char(20) not null, age int, sex char(1), income float, primary key " \
            "(name))"

# 执行sql语句
cursor.execute(sql_table)

# 插入数据
sql_in = "insert into test(name, age, sex, income) values ('Playboy', 25, 'M', 3000)"

try:
    cursor.execute(sql_in)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 修改数据
cursor.execute("update test set age='20' where name = '%s'" % ('Playboy'))
db.commit()

# 删除数据
sql_del = "delete from test where age > '%d'" % (18)
cursor.execute(sql_del)
db.commit()

# 关闭数据库
db.close()

