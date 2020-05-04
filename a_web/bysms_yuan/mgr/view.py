from django.core.paginator import Paginator, EmptyPage
from django.db import transaction
from django.db.models import F,Q
from django.http import JsonResponse, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.views import View
import json,traceback
from common.models import Order, OrderMedicine, Medicine, Customer


class signin(View):
    # 登录处理
    def post(self,request):
        # 从 HTTP POST 请求中获取用户名、密码参数
        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        # 使用 Django auth 库里面的 方法校验用户名、密码
        user = authenticate(username=userName, password=passWord)

        # 如果能找到用户，并且密码正确
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    # 在session中存入用户类型
                    request.session['usertype'] = 'mgr'

                    return JsonResponse({'ret': 0})
                else:
                    return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
            else:
                return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

        # 否则就是用户名、密码有误
        else:
            return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})

    # 登出处理

class signout(View):
    def get(self,request):
        # 使用登出方法
        logout(request)
        return JsonResponse({'ret': 0})

class OrderView(View):
    def get(self, request):
        action = request.GET.get("action")#必填参数
        # 要获取的第几页
        pagenum = request.GET.get("pagenum")
        # 每页要显示多少条记录
        pagesize = request.GET.get("pagesize")
        # 查看是否有 关键字 搜索 参数
        keywords = request.GET.get('keywords')

        # 返回一个 QuerySet 对象 ，包含所有的表记录
        if action !="list_order" or pagenum is None or pagesize is None:
            return JsonResponse({'ret': 3, 'msg': f'参数不全'})
        try:

            qs = Order.objects \
                .annotate(
                customer_name=F('customer__name')
            ) \
                .values(
                'id', 'name', 'create_date',
                'customer_name',
                'medicinelist'
            ).order_by('id')



            if keywords:
                conditions = [Q(name__contains=one) for one in keywords.split(' ') if one]
                query = Q()
                for condition in conditions:
                    query &= condition
                qs = qs.filter(query)

            # 使用分页对象，设定每页多少条记录
            pgnt = Paginator(qs, pagesize)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgnt.page(pagenum)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return JsonResponse({'ret': 0, 'retlist': retlist, 'total': pgnt.count})

        except EmptyPage:
            return JsonResponse({'ret': 0, 'retlist': [], 'total': 0})
        except:
            return JsonResponse({'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'})

    def post(self,request):
        info = json.loads(request.body)
        data = info['data']
        with transaction.atomic():
            medicinelist  = data['medicinelist']

            new_order = Order.objects.create(name=data['name'],
                customer_id=data['customerid'],
                # 写入json格式的药品数据到 medicinelist 字段中
                medicinelist=json.dumps(medicinelist,ensure_ascii=False),)

            batch = [OrderMedicine(order_id=new_order.id,
                                   medicine_id=medicine['id'],
                                   amount=medicine['amount'])
                     for medicine in medicinelist]

            OrderMedicine.objects.bulk_create(batch)

        return JsonResponse({'ret': 0, 'id': new_order.id})

    def delete(self,request):
        # 获取订单ID
        info = json.loads(request.body)
        oid = info['id']
        try:

            one = Order.objects.get(id=oid)
            with transaction.atomic():

                # 一定要先删除 OrderMedicine 里面的记录
                OrderMedicine.objects.filter(order_id=oid).delete()
                # 再删除订单记录
                one.delete()

            return JsonResponse({'ret': 0, 'id': oid})

        except Order.DoesNotExist:
            return JsonResponse({
                'ret': 1,
                'msg': f'id 为`{oid}`的订单不存在'
            })
        except:
            err = traceback.format_exc()
            return JsonResponse({'ret': 1, 'msg': err})

class MedicinesView(View):
    def get(self,request):

        action = request.GET.get("action")#必填参数
        # 要获取的第几页
        pagenum = request.GET.get("pagenum")
        # 每页要显示多少条记录
        pagesize = request.GET.get("pagesize")


        # 返回一个 QuerySet 对象 ，包含所有的表记录
        if action !="list_medicine" or pagenum is None or pagesize is None:
            return JsonResponse({'ret': 3, 'msg': f'参数不全'})
        try:
            # 返回一个 QuerySet 对象 ，包含所有的表记录
            qs = Medicine.objects.values().order_by('id')

            # 查看是否有 关键字 搜索 参数
            keywords = request.GET.get('keywords')
            if keywords:
                conditions = [Q(name__contains=one) for one in keywords.split(' ') if one]
                query = Q()
                for condition in conditions:
                    query &= condition
                qs = qs.filter(query)

            # 使用分页对象，设定每页多少条记录
            pgnt = Paginator(qs, pagesize)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgnt.page(pagenum)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return JsonResponse({'ret': 0, 'retlist': retlist, 'total': pgnt.count})

        except EmptyPage:
            return JsonResponse({'ret': 0, 'retlist': [], 'total': 0})

        except:
            return JsonResponse({'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'})

    def post(self,request):
        info = json.loads(request.body)
        data = info['data']

        # 从请求消息中 获取要添加客户的信息
        # 并且插入到数据库中
        medicine = Medicine.objects.create(name=data['name'] ,
                                sn=data['sn'] ,
                                desc=data['desc'])


        return JsonResponse({'ret': 0, 'id':medicine.id})

    def put(self,request):

        # 从请求消息中 获取修改客户的信息
        # 找到该客户，并且进行修改操作
        info = json.loads(request.body)
        medicineid = info['id']
        newdata = info['newdata']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            medicine = Medicine.objects.get(id=medicineid)
        except Medicine.DoesNotExist:
            return  {
                    'ret': 1,
                    'msg': f'id 为`{medicineid}`的药品不存在'
            }


        if 'name' in  newdata:
            medicine.name = newdata['name']
        if 'sn' in  newdata:
            medicine.sn = newdata['sn']
        if 'desc' in  newdata:
            medicine.desc = newdata['desc']

        # 注意，一定要执行save才能将修改信息保存到数据库
        medicine.save()

        return JsonResponse({'ret': 0})


    def delete(self,request):
        info = json.loads(request.body)
        medicineid = info['id']


        try:
            # 根据 id 从数据库中找到相应的药品记录
            medicine = Medicine.objects.get(id=medicineid)
        except Medicine.DoesNotExist:
            return  {
                    'ret': 1,
                    'msg': f'id 为`{medicineid}`的客户不存在'
            }

        # delete 方法就将该记录从数据库中删除了
        medicine.delete()

        return JsonResponse({'ret': 0})

class CustomerView(View):

    def get(slef,request):
        action = request.GET.get("action")#必填参数
        # 要获取的第几页
        pagenum = request.GET.get("pagenum")
        # 每页要显示多少条记录
        pagesize = request.GET.get("pagesize")


        # 返回一个 QuerySet 对象 ，包含所有的表记录
        if action !="list_customer" or pagenum is None or pagesize is None:
            return JsonResponse({'ret': 3, 'msg': f'参数不全'})
        try:
            # 返回一个 QuerySet 对象 ，包含所有的表记录
            qs = Customer.objects.values().order_by('id')

            # 查看是否有 关键字 搜索 参数
            keywords = request.GET.get('keywords')
            if keywords:
                conditions = [Q(name__contains=one) for one in keywords.split(' ') if one]
                query = Q()
                for condition in conditions:
                    query &= condition
                qs = qs.filter(query)

            # 使用分页对象，设定每页多少条记录
            pgnt = Paginator(qs, pagesize)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgnt.page(pagenum)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return JsonResponse({'ret': 0, 'retlist': retlist, 'total': pgnt.count})

        except EmptyPage:
            return JsonResponse({'ret': 0, 'retlist': [], 'total': 0})

        except:
            return JsonResponse({'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'})

    def post(self,request):

        info = json.loads(request.body)
        data = info['data']

        # 从请求消息中 获取要添加客户的信息
        # 并且插入到数据库中
        # 返回值 就是对应插入记录的对象
        record = Customer.objects.create(name=data['name'],
                                         phonenumber=data['phonenumber'],
                                         address=data['address'])

        return JsonResponse({'ret': 0, 'id': record.id})

    def put(self,request):
        # 从请求消息中 获取修改客户的信息
        # 找到该客户，并且进行修改操作
        info = json.loads(request.body)
        customerid = info['id']
        newdata = info['newdata']
        try:
            # 根据 id 从数据库中找到相应的客户记录
            customer = Customer.objects.get(id=customerid)
        except Customer.DoesNotExist:
            return {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
            }

        if 'name' in newdata:
            customer.name = newdata['name']
        if 'phonenumber' in newdata:
            customer.phonenumber = newdata['phonenumber']
        if 'address' in newdata:
            customer.address = newdata['address']

        # 注意，一定要执行save才能将修改信息保存到数据库
        customer.save()

        return JsonResponse({'ret': 0})

    def delete(self,request):

        info = json.loads(request.body)
        customerid = info['id']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            customer = Customer.objects.get(id=customerid)
        except Customer.DoesNotExist:
            return {
                'ret': 1,
                'msg': f'id 为`{customerid}`的客户不存在'
            }

        # delete 方法就将该记录从数据库中删除了

        order_id = Order.objects.filter()
        print(order_id)
        if order_id is not None:
            return HttpResponse({'ret': 1, 'msg': '此用户有订单,不可以删除'})

        customer.delete()

        return JsonResponse({'ret': 0})
