import requests
temp='a1=qwe;a2=rty;a3=asd'
url = "http://www.baidu.com/"

cookie_list = temp.split(';')


#列表生成式
cookies = {cookie.split('=')[0]:cookie.split('=')[1]for cookie in cookie_list}

print(cookies)


# 传统方法
cookie_dit = {}
for c in cookie_list:
    cookie_dit[c.split('=')[0]] = c.split('=')[1]

print(cookie_dit)

