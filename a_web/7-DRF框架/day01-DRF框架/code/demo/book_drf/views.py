from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from book_drf.serializer import BookSerialzier
from books.models import BookInfo


class Books(View):

    def get(self,request):
        # 1、查询所有图书对象
        books = BookInfo.objects.all()

        ser=BookSerialzier(books,many=True)

        return JsonResponse(ser.data, safe=False)


class Book(View):

    def get(self,request):
        book=BookInfo.objects.get(id=1)
        ser = BookSerialzier(book)

        return JsonResponse(ser.data)
