import json
import datetime
import traceback

from django import http
from django.http import JsonResponse
from django.views import View
from mgr.utils.sql_con import SelectDetailView


class OrderView(SelectDetailView,View):
    def get(self,request):
        # 查询操作
        action = request.GET.get("action")#必填参数
        # 要获取的第几页
        pagenum = request.GET.get("pagenum")
        # 每页要显示多少条记录
        pagesize = request.GET.get("pagesize")

        # 查看是否有 关键字 搜索 参数
        keywords = request.GET.get('keywords')

        page_start=int(pagenum)*int(pagesize)-int(pagesize)#每页开始位置
        page_end=int(pagenum)*int(pagesize)#每页结束位置

        # 返回一个 QuerySet 对象 ，包含所有的表记录
        if action !="list_order" or pagenum is None or pagesize is None:
            return JsonResponse({'ret': 3, 'msg': f'参数不全'})

        detail="select o.id,o.name,o.create_date,o.medicinelist,c.name from Order as o inner join Customer as c " \
               "where o.customer_id=c.id and o.name like '%{}%' limit {},{}".format(keywords,page_start,page_end)
        num_sql = "select count(*) from Order"
        num = self.select_one(num_sql)
        retlist=self.select_many(detail)
        retlist_list=[]
        for ret in retlist:
            retlist_dict={}
            retlist_dict["id"]=ret[0]
            retlist_dict["name"]=ret[1]
            retlist_dict["create_date"]=ret[2]
            retlist_dict["medicinelist"]=ret[3]
            retlist_dict["customer_name"]=ret[4]
            retlist_list.append(retlist_dict)

        return http.JsonResponse({'ret': 0,'retlist':retlist_list,'total': num[0]})

    def post(self,request):
        info = json.loads(request.body.decode())
        data = info['data']
        name = data['name']
        create_date=datetime.datetime.now()
        medicinelist=data['medicinelist']#list
        for m in medicinelist:
            if "amount" not in m:
                m["amount"]=1
        medicinestr = str(medicinelist).replace("'",'"')
        customer_id = data['customerid']

        add_sql = "insert into Order (name, create_date, medicinelist, customer_id) values ('{}','{}','{}','{}')".format(name,create_date,medicinestr,customer_id)
        #add_sql = '''insert into 'Order' (name, create_date, medicinelist, customer_id) values ('%s','%s','%s','%d')''' % (name,create_date,medicinelist,customer_id)
        self.insert_one(add_sql)
        order_id="select MAX(id) from Order"
        order_id = self.select_one(order_id)#订单id

        lists = [(med["id"], int(med["amount"]),order_id[0]) for med in medicinelist]
        add_sql2 = "insert  into OrderMedicine (amount,medicine_id,order_id) values (%s,%s,%s)"
        self.insert_many(add_sql2,lists)
        return JsonResponse({'ret': 0, 'id': order_id})

    def delete(self,request):
        info = json.loads(request.body)
        oid = info['id']
        try:
            sql = "delete from OrderMedicine where  order_id = {}".format(oid)
            self.delete_many(sql)
            sql = "delete from Order where id = {}".format(oid)
            self.delete_one(sql)
            return JsonResponse({'ret': 0, 'id': oid})
        except:
            err = traceback.format_exc()
            return JsonResponse({'ret': 1, 'msg': err})


class MedicinesView(SelectDetailView,View):

    def get(self,request):
        # 查询操作
        action = request.GET.get("action")#必填参数
        # 要获取的第几页
        pagenum = request.GET.get("pagenum")
        # 每页要显示多少条记录
        pagesize = request.GET.get("pagesize")

        # 查看是否有 关键字 搜索 参数
        keywords = request.GET.get('keywords')

        page_start=int(pagenum)*int(pagesize)-int(pagesize)#每页开始位置
        page_end=int(pagenum)*int(pagesize)#每页结束位置

        # 返回一个 QuerySet 对象 ，包含所有的表记录
        if action !="list_medicine" or pagenum is None or pagesize is None:
            return JsonResponse({'ret': 3, 'msg': f'参数不全'})

        detail="select m.id,m.name,m.sn,m.desc from Medicine as m " \
               "where  m.name like '%{}%' limit {},{}".format(keywords,page_start,page_end)
        num_sql = "select count(*) from Medicine"
        num = self.select_one(num_sql)
        retlist=self.select_many(detail)
        retlist_list=[]
        for ret in retlist:
            retlist_dict={}
            retlist_dict["id"]=ret[0]
            retlist_dict["name"]=ret[1]
            retlist_dict["sn"]=ret[2]
            retlist_dict["desc"]=ret[3]
            retlist_list.append(retlist_dict)

        return http.JsonResponse({'ret': 0,'retlist':retlist_list,'total': num[0]})

    def post(self, request):
        info = json.loads(request.body.decode())
        data = info['data']
        name = data['name']
        desc = data['desc']
        sn = data['sn']

        add_sql = "insert into Medicine (name, desc, sn) values ('{}','{}','{}')".format(
            name, desc, sn)
        self.insert_one(add_sql)
        medicine_id = "select MAX(id) from Medicine"
        medicine_id = self.select_one(medicine_id)  # 订单id
        return JsonResponse({'ret': 0, 'id': medicine_id[0]})

    def delete(self,request):
        info = json.loads(request.body)
        mid = info['id']
        try:
            sql = "delete from Medicine where  id = {}".format(mid)
            self.delete_one(sql)
            return JsonResponse({'ret': 0, 'id': mid})
        except:
            err = traceback.format_exc()
            return JsonResponse({'ret': 1, 'msg': err})

    def put(self,request):
        # 从请求消息中 获取修改客户的信息
        # 找到该客户，并且进行修改操作
        info = json.loads(request.body)
        medicine_id = info['id']
        newdata = info['newdata']
        name = newdata['name']
        desc = newdata['desc']
        sn = newdata['sn']

        sql = "select id from Medicine where  id = {}".format(medicine_id)
        id=  self.select_one(sql)
        if id[0] is None:
            err = traceback.format_exc()
            return JsonResponse({'ret': 1, 'msg': err})
        sql = "update Medicine set name ='{}',desc ='{}',sn ='{}' where id = {}".format(name,desc,sn,medicine_id)
        self.update_one(sql)
        return JsonResponse({'ret': 0})


class CustomerView(SelectDetailView,View):

    def get(self,request):
        # 查询操作
        action = request.GET.get("action")#必填参数
        # 要获取的第几页
        pagenum = request.GET.get("pagenum")
        # 每页要显示多少条记录
        pagesize = request.GET.get("pagesize")

        # 查看是否有 关键字 搜索 参数
        keywords = request.GET.get('keywords')

        page_start=int(pagenum)*int(pagesize)-int(pagesize)#每页开始位置
        page_end=int(pagenum)*int(pagesize)#每页结束位置

        # 返回一个 QuerySet 对象 ，包含所有的表记录
        if action !="list_customer" or pagenum is None or pagesize is None:
            return JsonResponse({'ret': 3, 'msg': f'参数不全'})

        detail="select c.id,c.name,c.phonenumber,c.address from Customer as c " \
               "where  c.name like '%{}%' limit {},{}".format(keywords,page_start,page_end)
        num_sql = "select count(*) from Customer"
        num = self.select_one(num_sql)
        retlist=self.select_many(detail)
        retlist_list=[]
        for ret in retlist:
            retlist_dict={}
            retlist_dict["id"]=ret[0]
            retlist_dict["name"]=ret[1]
            retlist_dict["phonenumber"]=ret[2]
            retlist_dict["address"]=ret[3]
            retlist_list.append(retlist_dict)

        return http.JsonResponse({'ret': 0,'retlist':retlist_list,'total': num[0]})

    def post(self, request):
        info = json.loads(request.body.decode())
        data = info['data']
        name = data['name']
        phonenumber = data['phonenumber']
        address = data['address']

        add_sql = "insert into Customer (name, phonenumber, address) values ('{}','{}','{}')".format(
            name, phonenumber, address)
        self.insert_one(add_sql)
        Customer_id = "select MAX(id) from Customer"
        Customer_id = self.select_one(Customer_id)  # 订单id
        return JsonResponse({'ret': 0, 'id': Customer_id[0]})

    def delete(self,request):
        info = json.loads(request.body)
        cid = info['id']
        try:
            sql = "delete from Customer where id = {}".format(cid)
            self.delete_one(sql)
            return JsonResponse({'ret': 0, 'id': cid})
        except:
            err = traceback.format_exc()
            return JsonResponse({'ret': 1, 'msg': err})

    def put(self,request):
        # 从请求消息中 获取修改客户的信息
        # 找到该客户，并且进行修改操作
        info = json.loads(request.body)
        custom_id = info['id']
        sql = "select * from Customer where  id = {}".format(custom_id)
        cus=  self.select_one(sql)
        if cus[0] is None:
            err = traceback.format_exc()
            return JsonResponse({'ret': 1, 'msg': err})
        oldname=cus[1]
        oldphonenumber = cus[2]
        oldaddress = cus[3]
        newdata = info['newdata']
        name = oldname
        phonenumber = oldphonenumber
        address = oldaddress
        if 'name' in newdata:
            name = newdata['name']
        if 'phonenumber' in newdata:
            phonenumber = newdata['phonenumber']
        if 'address' in newdata:
            address = newdata['address']

        sql = "update Customer set name ='{}',phonenumber ='{}',address ='{}' where id = {}".format(name,phonenumber,address,custom_id)
        self.update_one(sql)
        return JsonResponse({'ret': 0})

    # def put(self,request):#mysql支持这个语法,sqlite3不支持
    #     # 从请求消息中 获取修改客户的信息
    #     # 找到该客户，并且进行修改操作
    #     info = json.loads(request.body)
    #     id = info['id']
    #     table='Customer'
    #     newdata = info['newdata']
    #     newdata['id'] = id
    #     self.insert_update(table,newdata)
    #     return JsonResponse({'ret': 0})
