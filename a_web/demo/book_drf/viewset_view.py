from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from book_drf.serializer import BookSerializer
from books.models import BookInfo
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class Books(ViewSet):
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

class BookDRFView(ViewSet):

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

    def retrieve(self,request,pk):
        book=BookInfo.objects.get(id=pk)

        ser=BookSerializer(book)

        return Response(ser.data)
