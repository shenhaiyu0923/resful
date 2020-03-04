#coding:utf-8
import requests
#
# # url地址中的协议不能缺失
# url = "http://www.baidu.com"
#
# response = requests.get(url)
#
# print(response.cookies)
#
# cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
# print(cookie_dict)
#
# cookie_jar = requests.utils.cookiejar_from_dict(cookie_dict)
# print(cookie_jar)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}
url = 'https://www.youtube.com/'
response = requests.get(url, timeout=3, headers=headers)
