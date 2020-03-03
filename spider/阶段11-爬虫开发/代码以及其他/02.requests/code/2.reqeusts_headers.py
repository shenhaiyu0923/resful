#coding:utf-8
import requests

# url地址中的协议不能缺失
url = "http://www.baidu.com"

response1 = requests.get(url)
print(response1.request.headers)
print(len(response1.content))


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
response2 = requests.get(url, headers=headers)


print(response2.request.headers)
print(len(response2.content))