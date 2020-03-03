import sqlite3
# 1.硬盘上创建连接
global DB_FILE_PATH
global SHOW_SQL
con = sqlite3.connect('db.sqlite3')
# 获取cursor对象
cur = con.cursor()

sql = """update tb_books set btitle={} where id={}""".format(444,1)

cur.execute(sql)
# 获取所有数据
con.commit()