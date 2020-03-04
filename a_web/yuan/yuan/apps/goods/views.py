from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.db import connection
import sqlite3




# class DetailView(View):
#
#     def get(self,request):
#
#         # 查询操作
#         cursor = connection.cursor()
#         cursor.execute("select * from test01 where id = 1")
#
#         raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
#         #a=cursor.fetchall()  # 读取所有
#         sex=raw[3]
#         print(sex)
#         response = http.JsonResponse({'content':raw,'sex':sex},json_dumps_params={'ensure_ascii':False})
#         return response
#
#         # context = {
#         #     'sex': sex,
#         # }
#         # print(context)
#         # return render(request, 'detail1.html', context)



class DetailView(View):

    def get(self,request):

        conn = sqlite3.connect("test.db")

        cursor = conn.cursor()

        sql = 'select * from test01'
        cursor.execute(sql)
        values = cursor.fetchall()
        print(values)
        cursor.close()
        conn.close()
        response = http.JsonResponse({"values":values},json_dumps_params={'ensure_ascii':False})
        return response