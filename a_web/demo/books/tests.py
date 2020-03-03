from django.test import TestCase
import requests,json
# Create your tests here.
from pprint import pprint as print
def books():#查询所有图书
    url = 'http://127.0.0.1:8004/books/'
    r=requests.get(url)
    print(r.json())
    return r

def booksadd():#查询所有图书
    url = 'http://127.0.0.1:8004/books/'
    data={"btitle": "射雕英雄传1","bpub_date": "1980-05-01"}
    data=json.dumps(data)#将字典转化成json
    r=requests.post(url,data=data)
    print(r.json())
    return r

def bookone():#查询一个图书
    url = 'http://127.0.0.1:8004/books/7'

    r=requests.get(url,)
    print(r.json())
    return r

def bookput():#查询所有图书
    url = 'http://127.0.0.1:8004/books/1'
    data={
    "btitle": "射雕英雄传8",
    "bpub_date": "1980-05-01",
}
    data=json.dumps(data)#将字典转化成json
    r=requests.put(url,data=data)
    print(r.json())
    return r

def bookdel():#查询一个图书
    url = 'http://127.0.0.1:8004/books/7'

    r=requests.delete(url,)
    print(r.json())
    return r


# books()#查询所有图书
# booksadd()#增加图书
# bookone()#查询一个图书
# bookput() #修改一个图书
# bookdel()  #修改


