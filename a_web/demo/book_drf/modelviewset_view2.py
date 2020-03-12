from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    # serializer_class = BookSerializer  # 指定当前类视图使用的序列化器

    # 这种不常用,一般一个类对应一个序列化器
    def get_serializer_class(self):
        if self.action =='lastdata':
            return BookSerializer
        elif self.action=='create':
            return BookSerializer
        else:
            return BookSerializer

    @action(methods=['get'],detail=True)#detail=True 可以带参数
    def lastdata(self,request,pk):
        print(self.action)
        book=BookInfo.objects.get(id=pk)
        ser=self.get_serializer(book)
        return Response(ser.data)