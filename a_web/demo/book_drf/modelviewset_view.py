from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器