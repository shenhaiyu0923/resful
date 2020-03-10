import json

from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Create your views here.
from book_drf.serializer import BookSerialzier
from books.models import BookInfo


class Books(ViewSet):
    def list(self, request):
        # 1、查询所有图书对象
        books = BookInfo.objects.all()

        ser = BookSerialzier(books, many=True)

        return Response(ser.data)

    def create(self, request):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        ser = BookSerialzier(data=data)
        ser.is_valid()  # 验证方法

        # 3、保存数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)


class BookDRFView(ViewSet):
    """
        获取单一和更新和删除
    """

    def update(self, request, pk):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)
        ser = BookSerialzier(book, data=data)
        ser.is_valid()
        # 3、更新数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)


    def lastdata(self,request,pk):
        book=BookInfo.objects.get(id=pk)

        ser=BookSerialzier(book)

        return Response(ser.data)


class Book(ViewSet):
    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerialzier(book)

        return Response(ser.data)
