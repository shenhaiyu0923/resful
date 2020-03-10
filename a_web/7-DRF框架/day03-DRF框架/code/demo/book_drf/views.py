import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from book_drf.serializer import BookSerialzier
from books.models import BookInfo
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView


class Books(View):
    
    def get(self,request):
        # 1、查询所有图书对象
        books = BookInfo.objects.all()

        ser= BookSerialzier(books,many=True)

        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        ser= BookSerialzier(data=data_dict)
        ser.is_valid() # 验证方法

        # 3、保存数据
        ser.save()
        # 4、返回结果
        return JsonResponse(ser.data)




class Book(View):

    def get(self,request):
        book=BookInfo.objects.get(id=1)
        ser = BookSerialzier(book)

        return JsonResponse(ser.data)


class BookDRFView(View):
    """
        获取单一和更新和删除
    """

    def put(self, request, pk):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)
        ser=BookSerialzier(book,data=data_dict)
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

        book.is_delete=True
        book.save()
        return JsonResponse({})
