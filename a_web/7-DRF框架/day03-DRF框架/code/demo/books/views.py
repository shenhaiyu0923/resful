from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from books.models import BookInfo
import json
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView

# Create your views here.
class BooksView(View):
    """
     获取所有和保存
    """

    def get(self, request):

        # 1、查询所有图书对象
        books = BookInfo.objects.all()

        # 2、返回图书数据 [{},{}.{}]
        book_list = []
        for book in books:
            book_list.append(
                {
                    'id': book.id,
                    'btitle': book.btitle,
                    'bread': book.bread,
                    'bcomment': book.bcomment,
                    'bpub_date': book.bpub_date,
                }
            )
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')

        if bpub_date is None or bpub_date is None:
            return JsonResponse({'error': '错误信息'}, status=400)
        # 3、保存数据
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        # 4、返回结果
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )


class BookView(View):
    """
        获取单一和更新和删除
    """

    def get(self, request, pk):
        # 1、查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)

        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )

    def put(self, request, pk):
        # 1、获取前端数据
        data = request.body.decode()
        data_dict = json.loads(data)
        # 2、验证数据
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')

        if bpub_date is None or bpub_date is None:
            return JsonResponse({'error': '错误信息'}, status=400)
        # 3、更新数据
        try:
            book=BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        book.btitle=btitle
        book.bpub_date=bpub_date
        book.save()
        # 4、返回结果
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )

    def delete(self, request, pk):
        # 1、查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)

        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        book.is_delete=True
        book.save()
        return JsonResponse({})


