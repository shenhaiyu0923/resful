
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from books.models import BookInfo
# Create your views here.
from book_drf.serializer import BookSerialzier



class Books(ListCreateAPIView):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器

class BookDRFView(RetrieveUpdateDestroyAPIView):
    """
        获取单一和更新和删除
    """
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerialzier  # 指定当前类视图使用的序列化器

class Book(GenericAPIView):
    def get(self, request):
        book = BookInfo.objects.get(id=1)
        ser = BookSerialzier(book)

        return Response(ser.data)
