#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 4:08 PM
# @Author  : playboy


from MysqlHelper import *

# 连接person数据库
my_db = MysqlHelper('10.211.55.3', 'root', 'chaoer1314', 'person')

# 新建person表
# 如果表存在先删除
my_db.create_table("drop table if exists person")
my_db.create_table("create table if not exists person(name char(20), age int, PRIMARY KEY (name))")

# 在person表中插入数据
my_db.insert_data("insert into person(name, age) VALUES ('playboy', 20)")
my_db.insert_data("insert into person(name, age) VALUES ('aaa',37)")
my_db.insert_data("insert into person(name, age) VALUES ('bbb',17)")

# 修改数据
my_db.update_data("update person set age='25' where name = '%s' " % ('playboy'))

# 查询数据
ret = my_db.find_data("select * from person WHERE age > '%d'" % (20))
print(ret)

# 删除数据
my_db.delete_data("delete from person WHERE age > '%d'" % (20))

ret1 = my_db.find_data("select * from person WHERE age > '%d'" % (20))
print(ret1)

# 关闭数据库
my_db.close_data()
