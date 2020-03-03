from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from book_drf.serializer import BookSerializer
from books.models import BookInfo
# Create your views here.

class Books(View):

    def get(self,request):
        # 查询所有图书对象

        books = BookInfo.objects.all()
        ser = BookSerializer(books,many=True)# 查询多个
        return JsonResponse(ser.data,safe=False,json_dumps_params={'ensure_ascii':False})


class Book(View):

    def get(self,request):
        # 查询所有图书对象

        book = BookInfo.objects.get(id=1)
        ser = BookSerializer(book)##查询单个
        return JsonResponse(ser.data,safe=False,json_dumps_params={'ensure_ascii':False})