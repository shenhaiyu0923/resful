#coding:utf-8
import requests
import re
from pprint import pprint

def login():
    # url
    url = 'http://www.renren.com/PLogin.do'
    # session
    session = requests.session()#会话保持

    # headers
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    }

    # URL1 获取token
    url1='https://github.com/login'
    # 发送请求获取响应
    res_1 = session.get(url1).content.decode()
    #正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />',res_1)[0]
    print(token)

    # url2  登陆
    url2 = 'https://github.com/session'
    #构造表单数据

    # formdata
    formdata = {
    "commit": "Sign in",
    "utf8": "✓",
    "authenticity_token": token,
    "login": "shenhaiyu0923",
    "password": "guiji0923",
    "webauthn - support": "supported",
    "webauthn - iuvpaa - support": "supported",
    "return_to":"",
    "required_field_2788":"",
    "timestamp": "1582475942047",
    "timestamp_secret": "d4e16f11b12e1cdae80ef371d6e86094f7bcea0c4f07a4d130e92066c3b71767"
    }
    pprint(formdata)
    # 登录
    session.post(url2, data=formdata)

    #url3 验证
    url3 = 'https://github.com/shenhaiyu0923'
    response =session.get(url3)
    with open('github.html', 'wb')as f:
        f.write(response.content)

if __name__== '__main__':
    login()
