import json

from django.http import JsonResponse, HttpRequest
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response

# Create your views here.
from book_drf.serializer import BookSerialzier
from books.models import BookInfo


class Books(CreateModelMixin, ListModelMixin,GenericAPIView):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Book(GenericAPIView):
    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerialzier(book)

        return Response(ser.data)


class BookDRFView(GenericAPIView,UpdateModelMixin,DestroyModelMixin):
    """
        获取单一和更新和删除
    """

    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器

    def put(self, request, pk):
       return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)