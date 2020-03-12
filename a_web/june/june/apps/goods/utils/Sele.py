from django.views import View
from django.db import connection

class SelectDetailView(View):
    def gets(self,sql=None):
        # 查询操作
        cursor = connection.cursor()
        cursor.execute(sql)
        raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
        return raw


def gets(sql=None):
    # 查询操作
    cursor = connection.cursor()
    cursor.execute(sql)
    raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
    return raw