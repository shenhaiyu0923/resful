#coding:utf-8
import requests
import re

def login():
    # url
    url = 'http://www.renren.com/PLogin.do'
    # session
    session = requests.session()

    # headers
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    # formdata
    formdata = {
        'email': '17173805860',
        'password': '!QAZ2wsx#EDC'
    }

    # 登录
    session.post(url, data=formdata)

    # 验证登录
    response = session.get('http://www.renren.com/923768535/profile')
    print(response.url)
    print(re.findall('迷途',response.content.decode()))

login()