from django.http import JsonResponse
from book_drf.serializer import BookSerializer
from books.models import BookInfo
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class Books(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = BookInfo.objects.all() #指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  #指定当前类视图使用的序列化器
    def get(self,request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class Book(GenericAPIView):

    def get(self,request,pk):
        #  查询所有图书对象
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)##查询单个
        return Response(ser.data)


class BookDRFView(GenericAPIView,UpdateModelMixin,DestroyModelMixin):

    queryset = BookInfo.objects.all()  #指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  #指定当前类视图使用的序列化器


    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.delete(request,pk)