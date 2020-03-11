from book_drf.serializer import BookSerializer
from books.models import BookInfo
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin



class Books(ListCreateAPIView):
    queryset = BookInfo.objects.all() #指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  #指定当前类视图使用的序列化器

# class Book(GenericAPIView):
#
#     def get(self,request,pk):
#         #  查询所有图书对象
#         book = BookInfo.objects.get(id=pk)
#         ser = BookSerializer(book)##查询单个
#         return Response(ser.data)

class Book(RetrieveModelMixin,GenericAPIView):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器
    def get(self,request,pk):
        return self.get(request,pk)

class BookDRFView(RetrieveUpdateDestroyAPIView):
    """
        获取单一和更新和删除
    """
    queryset = BookInfo.objects.all()  #指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  #指定当前类视图使用的序列化器