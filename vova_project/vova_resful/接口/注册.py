import requests
import pprint
from time import sleep,ctime
import threading

   
def ztest_reg():#
    headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 9; vivo X21A Build/PKQ1.180819.001) [,1b8ba1836067773c,1578710372871-2164943907535087689] lq-App Vova 2.59.0 android"}
    params={
        "timezone":"Asia/Shanghai",
        "access_token":"",
        "s":2,
        "uid":0,
        "imei":"540000000045036",
        "imsi":"46007",
        "uuid":"340fee311994e386",
        "other":"zh;CN;0;46007;;;1;GMT+08:00;1;0",
        "version":"2.59.0",
        "currency":"USD",
        "is_new_user":0,
        "brand_country_code":"CN",
        "country_code":"CN",
        "sign":"c95fc29a226b66208446d70af8dd0ec1"
    }
    data={
        "app_device_id": "",
        "birthday":"",
        "event":"account",
        "firstRegister":"false",
        "first_name":"jin1",
        "last_name":"ui",
        "loginSuccessTo":0,
        "needCoinsDialog":"true",
        "notice_id":"",
        "password":"96e79218965eb72c92a549dd5a330112",
        "req_time":"1579656832",
        "sign":"e732d2dd9da876a1abd4537ca472d7bb",
        "type":"",
        "username":"t00001092@163.com"
    }
    url="http://api-t4.vova.com/en/v2/authentications"
    r=requests.post(url=url,
                    headers=headers,
                    params=params,
                    data=data,
                   )
    pprint.pprint(r.json())
ztest_reg()