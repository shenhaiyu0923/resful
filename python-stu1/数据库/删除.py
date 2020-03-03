#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "yuyan")

# 使用cursor()方法获取操作游标
cur = db.cursor()

# SQL 插入语句
sql = "DELETE FROM goods WHERE AGE > %s" % (11)
try:
   cur.execute(sql)
   db.commit()
   print("123")
except:
   db.rollback()
db.close()