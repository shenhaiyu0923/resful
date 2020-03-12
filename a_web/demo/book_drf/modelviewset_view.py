from django.db import DatabaseError
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo

class PageNum(PageNumberPagination):
    page_size = 2 #默认每页数量
    page_size_query_param = 'page_size'
    max_page_size = 4

class Books(ModelViewSet):
    """
    get:
    返回所有图书信息.

    post:
    新建图书.
    """
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器

    # 指定分页器
    # http://127.0.0.1:8001/books_drf/?page=2
    # http://127.0.0.1:8001/books_drf/?page=1&page_size=6
    pagination_class = PageNum

    # 过滤
    # http://127.0.0.1:8001/books_drf/?btitle=%E9%9B%AA%E5%B1%B1%E9%A3%9E%E7%8B%90
    filter_fields = ('btitle', 'bread')

    # 指定排序
    # http://127.0.0.1:8001/books_drf/?ordering=-bread    ordering是固定的
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'bread', 'bpub_date')

    @action(methods=['get'],detail=True)#子定义视图函数 detail=True 可以带参数
    def lastdata(self,request,pk):
        # http://127.0.0.1:8001/books_drf/1/lastdata
        #raise DatabaseError  测试数据库异常处理
        book=BookInfo.objects.get(id=pk)
        ser=BookSerializer(book)
        return Response(ser.data)