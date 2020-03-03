import requests

url = "http://www.baidu.com/"

response = requests.get(url)
print(len(response.content.decode()))  #计算长度


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

response1=requests.get(url,headers=headers,timeout=3)#带请求头参数,设置请求最大时间

print(len(response1.content.decode()))