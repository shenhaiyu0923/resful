import requests
import pprint
from time import sleep,ctime
import threading

   
def ft310227():
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android"}
    params={
        "timezone":"Asia/Shanghai",
        "access_token":"ZWE2MzI3NWJjMGUwNWE3OGFiYmM4ZGJkZjdlMmQwYmRfY2FjZTg4NzM0YTdkZDk3OWJiMTlkMmI5ODU2MGFhMTU=",
        "navigationBarHeight":"132",
        "s":"2",
        "uid":"16800818",
        "imsi":"46001",
        "lang":"en",
        "uuid":"1b8ba1836067773c",
        "statusBarHeight":"84",
        "0ther":"zh;CN;0;46001;;;0;GMT+08:00;2",
        "user_type":"2",
        "version":"2.48.1",
        "currency":"USD",
        "is_new_user":"0",
        "is_open_notification":"1",
        "webview":"1",
        "brand_country_code":"CN",
        "country_code":"CN",
        "h5_version":"1.0.3",
        "req_time":"1571746721",
        "sign":"21794d523c1aabc6e9d1441a4ab202c4",
    }
    data={
        "exchange_id": 3,
        "req_time":"1571746721",
        "sign":"ab48f484f24ba72dfea03b0acf4715c9"
    }
    r=requests.post('http://api-a1-t3.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                   data=data)
    pprint.pprint(r.json())

def ft310226():
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android"}
    params={
        "timezone":"Asia/Shanghai",
        "access_token":"NDc2MjMyZDJhMGU5YTZmZjAwZjQ1ODcwMzEwMjEzN2VfZWM4Nzk1YzBjNWVjZDEzM2YyMjZmMmQ4YzNiODFmOWQ=",#########
        "navigationBarHeight":"132",
        "s":"2",
        "uid":"16800816",########
        "imsi":"46001",
        "lang":"en",
        "uuid":"1b8ba1836067773c",
        "statusBarHeight":"84",
        "0ther":"zh;CN;0;46001;;;0;GMT+08:00;2",
        "user_type":"2",
        "version":"2.48.1",
        "currency":"USD",
        "is_new_user":"0",
        "is_open_notification":"1",
        "webview":"1",
        "brand_country_code":"CN",
        "country_code":"CN",
        "h5_version":"1.0.3",
        "req_time":"1571749661",##########
        "sign":"aa8ed22e1e156cebf0e15073f49717b1",
    }
    data={
        "exchange_id": 3,#############
        "req_time":"1571749661",############
        "sign":"e5bc5ffce9d49726e15ddad0933d98a8"##############
    }
    r=requests.post('http://api-a1-t3.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                   data=data)
    pprint.pprint(r.json())

def ft310225():
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1571715392822-1921536911056350291] lq-App Vova 2.48.1 android"}
    params={
        "timezone":"Asia/Shanghai",
        "access_token":"Zjg4N2VkZTE3YzE3MDRjY2M2YTg4M2E4ZWZjYjU0ODlfODM4Y2Y4ZjE5NDE2YjMyYTQwZmMxNjRhOGJiZjI4Njc=",#########
        "navigationBarHeight":"132",
        "s":"2",
        "uid":"16800817",########
        "imsi":"46001",
        "lang":"en",
        "uuid":"1b8ba1836067773c",
        "statusBarHeight":"84",
        "0ther":"zh;CN;0;46001;;;0;GMT+08:00;2",
        "user_type":"2",
        "version":"2.48.1",
        "currency":"USD",
        "is_new_user":"0",
        "is_open_notification":"1",
        "webview":"1",
        "brand_country_code":"CN",
        "country_code":"CN",
        "h5_version":"1.0.3",
        "req_time":"1571750080",##########
        "sign":"70163e00e79fba013305332cf6da4d99",
    }
    data={
        "exchange_id": 3,#############
        "req_time":"1571750080",############
        "sign":"fa5e1141944de6778141c0112cd90da3"###################
    }
    r=requests.post('http://api-a1-t3.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                   data=data)
    pprint.pprint(r.json())

def thread1_entry(nsec):
    time_test=10
    while time_test>1:
        print('ft310225',ctime())
        ft310225()
        time_test=time_test-1

def thread2_entry(nsec):
    time_test=10
    while time_test>1:
        print('ft310226',ctime())
        ft310226()
        time_test=time_test-1

def thread3_entry(nsec):
    time_test=10
    while time_test>1:
        print('ft310227',ctime())
        ft310227()
        time_test=time_test-1

if __name__=='__main__':
    t1 = threading.Thread(target=thread1_entry,args=(1,))#thread1_entry函数对象
    t2 = threading.Thread(target=thread2_entry,args=(2,))
    t3 = threading.Thread(target=thread3_entry,args=(2,))
    t1.start()#开启线程
    t2.start()
    t3.start()
    t1.join()#等待线程结束
    t2.join()
    t3.join()

