import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "test",charset='utf8')

# 使用cursor()方法获取操作游标
cur = db.cursor()

# SQL 插入语句
sql = "select * from xiao where id = 1"
try:
   cur.execute(sql)
   data = cur.fetchone()
   print("id","name","age","sex")
   print (data)
except:
    print("查询失败")
db.close()