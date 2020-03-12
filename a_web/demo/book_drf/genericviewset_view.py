from django.http import JsonResponse
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.response import Response
from book_drf.serializer import BookSerializer
from books.models import BookInfo
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class Books(GenericViewSet):
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器
    def list(self, request):
        # 1、查询所有图书对象
        books = BookInfo.objects.all()

        ser = BookSerializer(books, many=True)

        return Response(ser.data)

    def create(self, request):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        ser = BookSerializer(data=data)
        ser.is_valid()  # 验证方法

        # 3、保存数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)

class BookDRFView(GenericViewSet):
    """
        获取单一和更新和删除
    """
    queryset = BookInfo.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器
    def update(self, request, pk):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)
        ser = BookSerializer(book, data=data)
        ser.is_valid()
        # 3、更新数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)

    def destroy(self, request, pk):
        # 1、查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)

        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        #book.is_delete=True #逻辑删除
        #book.save()
        book.delete() #物理删除

        return Response({})

    def lastdata(self,request,pk):
        book=BookInfo.objects.get(id=pk)

        ser=BookSerializer(book)

        return Response(ser.data)

    def Retrieve(self,request,pk):
        book=BookInfo.objects.get(id=pk)

        ser=BookSerializer(book)

        return Response(ser.data)
