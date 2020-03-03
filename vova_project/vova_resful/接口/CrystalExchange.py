import requests
import pprint
from time import sleep,ctime
import threading

   #ft31022@tetx.com
def t0110():#钻石号
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1578710372871-2164943907535087689] lq-App Vova android"}
    params={
        "show_version":"yes",
        "timezone":"Asia/Shanghai",
        "access_token":"NmE0ZmIyY2UyM2ZmYTRjMWVkZmU0NmMxYjNmYmZkMDRfNWE0Zjc3ZjNiMzFhNzFlMmE3NTY1MDJkZGI5NTI3MGE=",
        "navigationBarHeight":"132",
        "s":"2",
        "uid":"6260778",
        "imsi":"",
        "lang":"en",
        "uuid":"1b8ba1836067773c",
        "statusBarHeight":"84",
        "0ther":"zh;CN;0;;;;0;GMT+08:00;2",
        "user_type":"2",
        "version":"2.58.0",
        "currency":"USD",
        "is_new_user":"0",
        "is_open_notification":"0",
        "webview":"1",
        "brand_country_code":"CN",
        "country_code":"CN",
        "h5_version":"1.0.3",
        "req_time":"1578654358",
        "sign":"7a3fa99b2745bde6bac6b9fbfc0950dc",
    }
    data={
        "exchange_id": 3,
        "req_time":"1578710696",
        "sign":"947787a3fd7d5b5f7b64efa898850357"
    }
    r=requests.post('http://api-a1-4.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                   data=data)
    pprint.pprint(r.json())
#t0110()








def zcapp():
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1578710372871-2164943907535087689] lq-App Vova android"}
    params={
        "show_version":"yes",
        "timezone":"Asia/Shanghai",
        "access_token":"NzkwMzhlN2Q2ZGY5MTU4ZmY0NzVhNWM5YTE2OWM4YjFfYWQwNzQ2MTAxNDc1M2Y3NGZmOTcyZjhlOGY5OThlMmQ=",
        "navigationBarHeight":"132",
        "s":"2",
        "uid":"6260778",
        "imsi":"",
        "lang":"en",
        "uuid":"1b8ba1836067773c",
        "statusBarHeight":"84",
        "0ther":"zh;CN;0;;;;0;GMT+08:00;2;0",
        "user_type":"2",
        "version":"2.59.0",
        "currency":"USD",
        "is_new_user":"0",
        "is_open_notification":"0",
        "webview":"1",
        "brand_country_code":"CN",
        "country_code":"CN",
        "h5_version":"1.0.3",
        "req_time":"1578712943",
        "sign":"636ef57a432bf793918e9738487fad3a",
    }
    data={
        "exchange_id": 3,
        "req_time":"1578712943",
        "sign":"636ef57a432bf793918e9738487fad3a"
    }
    r=requests.post('http://api-a1.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                   data=data)
    print(zcapp)
    pprint.pprint(r.json())
zcapp()



'''
/pt/v1/activity/freesale/crystalExchange?show_version=yes&timezone=America%2FSao_Paulo&access_token=
YTk4ZWNhYzc2MzA3NDllN2QyNTFlNjU3MWVhOWViYWZfM2E3ZWVjNzRlN2ExYmRlY2RlYTY4MDEwNGI4ZDNiNzU=
&navigationBarHeight=66&s=1&uid=75424889&imsi=72402&lang=pt&uuid=
f741dbe1f6b4972&statusBarHeight=36&other=pt%3BBR%3B0%3B72402%3B%3B%3B0%3BBRST%3B2&user_type=2&version=2.57.0&currency=
BRL&is_new_user=0&is_open_notification=1&webview=1&brand_country_code=BR&country_code=BR&h5_version=1.0.3
&req_time=1578524576&sign=e5cdca2b400a4028df9ce55bd6282436
'''





'''
 http://api-a1-t.vova.com/en/v1/activity/freesale/crystalExchange?show_version=yes&timezone=Asia%2FShanghai&access_token=MzZmNjZmMTk5YmEzMjliNDdlMTczNDIyYjAwZGFjNGNfMTdmMWJiYTZlZjdiYTc3M2IwYWMzNTI0ZmRlZGJiZmU%3D&navigationBarHeight=132&s=2&uid=16805551&imsi=&lang=en&uuid=1b8ba1836067773c&statusBarHeight=84&other=zh%3BCN%3B0%3B%3B%3B%3B0%3BGMT%2B08%3A00%3B2&user_type=2&version=2.58.0&currency=USD&is_new_user=0&is_open_notification=0&webview=1&brand_country_code=CN&country_code=CN&h5_version=1.0.3&req_time=1578710696&sign=7a3fa99b2745bde6bac6b9fbfc0950dc
'''


'''
{'code': 10040,
 'data': {'result': True},
 'msg': 'app_common_signature_auth_failure'}
'''