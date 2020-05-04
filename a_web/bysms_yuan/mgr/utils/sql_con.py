from django.views import View
from django.db import connection

cursor = connection.cursor()
class SelectDetailView(View):
    def select_many(self,sql=None):
        # 查询操作
        cursor.execute(sql)
        raw = cursor.fetchall()  # 返回结果行游标直读向前，读取全部
        return raw

    def select_one(self,sql=None):
        # 查询操作
        cursor.execute(sql)
        raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
        return raw

    def insert_many(self, sql=None,lists=None):
        cursor.executemany(sql,lists)
        connection.commit()
        #connection.rollback()

    def insert_one(self,sql=None):
        cursor.execute(sql)
        print(cursor.lastrowid)
        connection.commit()

    def update_many(self,sql=None):
        cursor.execute(sql)
        print(cursor.lastrowid)
        connection.commit()

    def update_one(self,sql=None):
        cursor.execute(sql)
        print(cursor.lastrowid)
        connection.commit()

    def delete_many(self,sql=None):
        cursor.execute(sql)
        print(cursor.lastrowid)
        connection.commit()

    def delete_one(self,sql=None):
        cursor.execute(sql)
        print(cursor.lastrowid)
        connection.commit()

    def insert_update(self,table=None,data=None):# mysql支持,sqlite3不支持这个语法
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,values=values)
        update = ','.join([" {key} = %s".format(key=key) for key in data])
        sql += update
        cursor.execute(sql, tuple(data.values()) * 2)
        print('Successful')
        connection.commit()

        print('Failed')
        connection.rollback()
        cursor.close()
        connection.close()




