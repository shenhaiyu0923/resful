from pprint import pprint as print
import requests
from hashlib import md5
import base64

class Duihuan:
    def __init__(self,):
        self.headers={
            "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0.1; VIVO X20 Build/V417IR) [,340fee311994e386,1583737416858-410961750665631264] lq-App Vova android",
        }
    def shuru(self):
        username=input("请输入用户名:")
        password=input("请输入用户名:")
        # username="ning@tetx.com"
        # password="111111"
        # 创建md5对象
        try:
            new_md5 = md5()
            # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
            new_md5.update(password.encode(encoding='utf-8'))
            # 加密
            m5 = new_md5.hexdigest()
            return username,m5
        except:
            print("密码初始化失败")

    def denglu(self,username,pwd):
        url="http://api-t2.vova.com/en/v2/authentications"
        params={
            "password":pwd,
            "username":username,
        }
        try:
            r=requests.get(url,params=params,headers=self.headers)
            r=r.json()
            uid=r['data']['uid']
            token=r['data']['access_token']
            return uid,token
        except:
            print("登陆失败")

    def zuanshi(self,uid,token):
        url='http://api-a1-t2.vova.com/en/v1/activity/freesale/crystalExchange'
        params={
            "access_token":token,
            "uid":uid,
        }
        data={
            "exchange_id": 1,
        }
        try:
            r=requests.post(url,headers=self.headers,params=params,
                           data=data)
            print(r.json())
            return r.json()
        except:
            print("钻石兑换失败")

    def run(self):
        username,password=self.shuru()
        uid,token=self.denglu(username,password)
        self.zuanshi(uid,token)

if __name__=='__main__':
    Duihuan=Duihuan()
    Duihuan.run()