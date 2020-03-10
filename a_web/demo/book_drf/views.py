import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from book_drf.serializer import BookSerializer
from book_drf.serializer import BookModelSerialzier
from books.models import BookInfo
# Create your views here.

class Books(View):

    def get(self,request):
        # 查询所有图书对象

        books = BookInfo.objects.all()
        ser = BookSerializer(books,many=True)# 查询多个
        return JsonResponse(ser.data,safe=False,json_dumps_params={'ensure_ascii':False})

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        ser= BookSerializer(data=data_dict)
        # ser.is_valid(raise_exception=True) # 验证方法
        ser.is_valid() # 验证方法
        #print(ser.validated_data)# 无效
        print(ser.errors)#

        # 3、保存数据
        ser.save()
        # 4、返回结果
        return JsonResponse(ser.data)

class Book(View):

    def get(self,request,pk):
        #  查询所有图书对象

        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)##查询单个
        print(ser.data)
        return JsonResponse(ser.data,safe=False,json_dumps_params={'ensure_ascii':False})


class BookDRFView(View):
    """
        获取单一和更新和删除
    """

    def get(self, request,pk):
        #  查询所有图书对象

        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)  ##查询单个
        return JsonResponse(ser.data, safe=False, json_dumps_params={'ensure_ascii': False})

    def put(self, request, pk):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)
        ser=BookSerializer(book,data=data_dict)
        ser.is_valid()
        # 3、更新数据
        ser.save()
        # 4、返回结果
        return JsonResponse(ser.data)

    def delete(self, request, pk):
        # 1、查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)

        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        #book.is_delete=True #逻辑删除
        #book.save()
        book.delete() #物理删除

        return JsonResponse({})