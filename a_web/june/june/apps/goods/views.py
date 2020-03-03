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
        #a=cursor.fetchall()  # 读取所有
        sex=raw[3]
        print(sex)
        #return http.JsonResponse({'content':raw,'sex':sex,"a":a})

        context = {
            'sex': sex,
        }
        print(context)
        return render(request, 'detail1.html', context)