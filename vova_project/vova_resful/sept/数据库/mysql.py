# 导入pymysql模块
import pymysql

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "123456", "rain")
# 使用 cursor() 方法创建一个游标对象 cursor
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from test_info"
try:
    cur.execute(sql)  # 执行sql语句
    results = cur.fetchall()  # 获取查询的所有记录
    print("id", "name", "age","sex","salary","vid")
    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        age = row[2]
        sex = row[3]
        salary = row[4]
        vid = row[5]
        print(row)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接

