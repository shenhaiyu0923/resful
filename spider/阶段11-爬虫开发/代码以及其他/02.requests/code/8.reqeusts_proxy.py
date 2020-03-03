#coding:utf-8
import requests

url = 'http://www.baidu.com'

proxy = {
    'http': 'http://101.231.104.82:80',
    'https': 'https://101.231.104.82:80',
    # 'https': 'https://1.192.246.63:9999',
}
proxy = {
    'http': 'http://user:pwd@101.231.104.82:80',
    'https': 'https://user:pwd@101.231.104.82:80',
    # 'https': 'https://1.192.246.63:9999',
}


response = requests.get(url, proxies=proxy)




