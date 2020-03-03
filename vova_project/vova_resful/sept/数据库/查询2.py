#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "yuyan",charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    print("fname,lname,age,sex,income")
    print(results)

except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()