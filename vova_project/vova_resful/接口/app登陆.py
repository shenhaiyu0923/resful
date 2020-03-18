from pprint import pprint as print
import requests
class Duihuan:
    def denglu(self):
        url="http://api-t2.vova.com/en/v2/authentications"
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept":"application/json",
            "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0.1; VIVO X20 Build/V417IR) [,340fee311994e386,1583737416858-410961750665631264] lq-App Vova 2.60.1 android",
            "Host":"api-t2.vova.com",
            "Accept-Encoding":"gzip",
            "Connection": "keep-alive",
        }
        params={
            "notice_id":"",
            "needCoinsDialog":"true",
            "password":"96e79218965eb72c92a549dd5a330112",
            "username":"ning@tetx.com",
            "event":"account",
            "loginSuccessTo":0,
            "firstRegister":"false",
            "timezone":"Asia/Shanghai",
            "access_token":"",
            "s":2,
            "uid":0,
            "imei":"540000000045036",
            "imsi":"46007",
            "uuid":"340fee311994e386",
            "other":"zh;CN;0;46007;;;1;GMT+08:00;1;0",
            "version":"2.60.1",
            "currency":"USD",
            "is_new_user":0,
            "brand_country_code":"CN",
            "country_code":"CN",
            "req_time":"1583737472",
            "sign":"c662c2717c735cf2b6b0ad4063b44450"
        }
        r=requests.get(url,params=params,headers=headers)
        return r.json()

        # r1 = genglu()
        # print(r1)
        # print(r1['data']['access_token'])

    def denglu2(self):
        url="http://api-t2.vova.com/en/v2/authentications"
        headers={
            "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0.1; VIVO X20 Build/V417IR) [,340fee311994e386,1583737416858-410961750665631264] lq-App Vova  android",
        }
        params={
            "password":"96e79218965eb72c92a549dd5a330112",
            "username":"ning@tetx.com",
        }
        r=requests.get(url,params=params,headers=headers)
        return r.json()

        # r1 = genglu()
        # print(r1)
        # print(r1['data']['access_token'])

    def zuanshi(self):
        headers={
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; VIVO X20 Build/V417IR) [,340fee311994e386,1583737416858-410961750665631264] lq-App Vova android",
        }
        params={
            "timezone":"Asia/Shanghai",
            "access_token":"NmNmNjQ5MzVkYWQ5ZTQ3M2UxMmQ4NWY5OWQ2ODliZjVfZjY4ZjYyZjE0OGNhNTZiMmViMmU0ZDE1ZWM1ZDE3NzQ=",
            "navigationBarHeight":"74",
            "s":"2",
            "uid":"16806825",
            "imsi":"46007",
            "lang":"en",
            "uuid":"340fee311994e386",
            "statusBarHeight":"41",
            "0ther":"zh;CN;0;46007;;;1;GMT+08:00;1;0",
            "user_type":"2",
            "version":"2.60.1",
            "currency":"USD",
            "is_new_user":"0",
            "is_open_notification":"1",
            "webview":"1",
            "brand_country_code":"CN",
            "country_code":"CN",
            "h5_version":"1.0.3",
            "req_time":"1583740824",
            "sign":"330eefef5c602504c363851e4e728afb",
        }
        data={
            "exchange_id": 1,
            "req_time":"1583740824",
            "sign":"cf417ac2000e875245dfcbac0b9af266"
        }
        r=requests.post('http://api-a1-t2.vova.com/en/v1/activity/freesale/crystalExchange',headers=headers,params=params,
                       data=data)
        print(r.json())

        return r.json()

Duihuan=Duihuan()

a=Duihuan.denglu()
print(a)
#Duihuan.zuanshi()

#exchange_id=1&req_time=1583740824&sign=cf417ac2000e875245dfcbac0b9af266