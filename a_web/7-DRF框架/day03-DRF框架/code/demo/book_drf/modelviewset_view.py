from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from book_drf.serializer import BookSerialzier
from books.models import BookInfo


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    # serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器


    def get_serializer_class(self):
        if self.action =='lastdata':
            return BookSerialzier
        elif self.action=='create':
            return BookSerialzier
        else:
            return BookSerialzier

    @action(methods=['get'],detail=True)
    def lastdata(self,request,pk):
        print(self.action)
        book=BookInfo.objects.get(id=pk)
        ser=self.get_serializer(book)
        return Response(ser.data)


