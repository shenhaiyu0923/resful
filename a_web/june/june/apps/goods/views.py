from django import http
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.db import connection

class DetailView(View):

    def get(self,request):
        # 查询操作
        cursor = connection.cursor()
        cursor.execute("select * from test01 where id = 1")
        raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
        cursor.execute("select * from test01")
        raw1=cursor.fetchall()  # 读取所有
        return http.JsonResponse({'content':raw,'content1':raw1,})

