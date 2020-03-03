import pymysql

# 2.插入操作
db = pymysql.connect(host="localhost", user="root",password="123456", db="rain", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()
sql_insert = """insert into user(id,username,password1) values(4,'liu','1234')"""

try:
    cur.execute(sql_insert)
    # 提交
    db.commit()
    print(123)
except Exception as e:
    # 错误回滚
    db.rollback()
finally:
    db.close()