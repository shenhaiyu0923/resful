#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "test")

# 使用cursor()方法获取操作游标
cur = db.cursor()

# SQL 插入语句
sql = "UPDATE xiao SET AGE = AGE + 1 WHERE SEX = '%s'" % ('男')
try:
   cur.execute(sql)
   db.commit()
   print("123")
except:
   db.rollback()
db.close()