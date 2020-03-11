from django.http import JsonResponse
from book_drf.serializer import BookSerializer
from books.models import BookInfo
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
# Create your views here.

class Books(GenericAPIView):
    queryset = BookInfo.objects.all() #指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  #指定当前类视图使用的序列化器
    def get(self,request):
        # 查询所有图书对象
        books = self.get_queryset() # 获取查询集中的所有的数据
        ser = self.get_serializer(books,many=True)# 使用指定序列化器，获取序列化器对象
        return Response(ser.data)
    def post(self, request):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        ser= self.get_serializer(data=data)
        # ser.is_valid(raise_exception=True) # 验证方法
        ser.is_valid() # 验证方法
        print(ser.validated_data)#验证正确后的数据
        #print(ser.errors)#

        # 3、保存数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)

class Book(GenericAPIView):

    def get(self,request,pk):
        #  查询所有图书对象
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)##查询单个
        return Response(ser.data)


class BookDRFView(GenericAPIView):
    """
        获取单一和更新和删除
    """
    queryset = BookInfo.objects.all()  #指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  #指定当前类视图使用的序列化器


    def put(self, request, pk):
        # 1、获取前端数据
        # data = request.body.decode()
        # data_dict = json.loads(data)
        data = request.data
        # 2、验证数据
        try:
            book = self.get_object() # 从查询集中获取指定的单一数据对象
        except:
            return JsonResponse({'error': '错误信息'}, status=400)
        ser=BookSerializer(book,data=data)
        ser.is_valid()
        # 3、更新数据
        ser.save()
        # 4、返回结果
        return Response(ser.data)

    def delete(self, request, pk):
        # 1、查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)

        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        #book.is_delete=True #逻辑删除
        #book.save()
        book.delete() #物理删除

        return Response({})