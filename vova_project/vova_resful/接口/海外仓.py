import requests
import pprint
from time import sleep,ctime
import threading

'''
1632818
'''
def biaozhuncang():#钻石号
    data={
        "sku_id": 4559981,
        "operate_type":"fix_data",
        "comment":"test",
        "change_amount":"+10"
    }
    r=requests.post('http://api-t4.vova.com/v1/notify/changeStorage',data=data)
    pprint.pprint(r.json())
biaozhuncang()

def haiwaicang():#海外仓
    data={
        "sku_id": 4559981,
        "operate_type":"fix_data",
        "comment":"test",
        "change_amount":"-0"
    }
    r=requests.post('http://api-t6.vova.com/v1/notify/changeFbvStorage',data=data)
    pprint.pprint(r.json())
haiwaicang()





