import requests
url = "http://www.baidu.com/"

response = requests.get(url)
print(response.cookies)
dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

jar_cookies = requests.utils.cookiejar_from_dict((dict_cookies))
print(jar_cookies)