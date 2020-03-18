import requests
import pprint
from time import sleep,ctime
import threading

   
def byhy():#过期信用卡支付
    data={
        "username": "byhy",
        "password": "88888888",
    }
    url='http://127.0.0.1:8001/api/mgr/signin'
    r=requests.post(url,data=data)
    pprint.pprint(r.json())
byhy()