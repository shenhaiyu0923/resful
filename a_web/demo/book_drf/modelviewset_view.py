from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器

    @action(methods=['get'],detail=True)#detail=True 可以带参数
    def lastdata(self,request,pk):
        book=BookInfo.objects.get(id=pk)
        ser=BookSerializer(book)
        return Response(ser.data)