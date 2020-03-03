import requests
import pprint
from time import sleep,ctime
import threading

def ft310225():
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android"}
    params={
        "access_token":"ZWE2MzI3NWJjMGUwNWE3OGFiYmM4ZGJkZjdlMmQwYmRfY2FjZTg4NzM0YTdkZDk3OWJiMTlkMmI5ODU2MGFhMTU=",#########
        "uid":"16800818",########
    }
    data={
        "exchange_id": 3,#############
    }
    r=requests.post('http://api-a1-t3.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                   data=data)
    pprint.pprint(r.json())

def thread1_entry(nsec):
    time_test=2
    while time_test>1:
        print('ft310225',ctime())
        ft310225()
        time_test=time_test-1



if __name__=='__main__':
    t1 = threading.Thread(target=thread1_entry,args=(1,))#thread1_entry函数对象
    t1.start()#开启线程
    t1.join()#等待线程结束


#  p1210@tetx.com