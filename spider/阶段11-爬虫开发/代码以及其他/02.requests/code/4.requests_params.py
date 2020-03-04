#coding:utf-8
import requests

# url中带参数
# url = 'https://www.baidu.com/s?wd=python'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers)
#
# with open('baidu.html', 'wb')as f:
#     f.write(response.content)


url = 'https://www.baidu.com/s'

params = {
    "wd": "python"
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

response = requests.get(url, params=params, headers=headers)

print(response.url)
with open('baidu2.html', 'wb')as f:
    f.write(response.content)