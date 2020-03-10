from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

class IndexView(View):

    def get(self,request):

        # 不分离
        # return render(request,'index.html',context={'name':'python'})

        return JsonResponse({'name':'python'})


class LoginView(View):

    def get(self,request):
        username=request.GET.get('username')
        # if version==1.0:
        # elif version==2.0:
        # 查询用户名
        return JsonResponse({'message':'ok'})


class BookView(View):
    def get(self,request,pk):

        return JsonResponse({'btitl':'西游记'})