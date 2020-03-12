from django import http
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.db import connection
from dev import cursor
from june.apps.goods.utils.Sele import SelectDetailView

# class DetailView(View):
#     def get(self,request):
#         # 查询操作
#         cursor = connection.cursor()
#         cursor.execute("select * from test01 where id = 1")
#         raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
#         cursor.execute("select * from test01")
#         raw1=cursor.fetchall()  # 读取所有
#         return http.JsonResponse({'content':raw,'content1':raw1,})



class DetailView(SelectDetailView,View):
    def get(self,request):
        # 查询操作
        sql="select * from test01 where id = {}".format(2)
        raw=self.gets(sql)
        return http.JsonResponse({'content':raw})


# class DetailView(View,):
#     def get(self,request):
#         # 查询操作
#         #cursor = connection.cursor()
#         cursor.execute("select * from test01 where id = 1")
#         raw = cursor.fetchone()  # 返回结果行游标直读向前，读取一条
#         cursor.execute("select * from test01")
#         raw1=cursor.fetchall()  # 读取所有
#         #print(raw1)# <class 'tuple'>
#         response = http.JsonResponse({'content':raw,'content1':raw1,},json_dumps_params={'ensure_ascii':False})
#         print(response.content.decode())
#         return response

