#coding:utf-8
import requests

# url地址中的协议不能缺失
url = "http://www.baidu.com"

response = requests.get(url)

# 查看响应url
print(response.url)
# 查看响应状态码
print(response.status_code)
# 查看响应头
print(response.headers)
# 查看请求头
print(response.request.headers)



# print(response.encoding)
# # 查看响应源码的str类型数据
# response.encoding = 'utf-8'
# print(response.text)
#
# # 查看响应源码的bytes类型数据
print(response.content.decode())

# 大部分网站默认使用utf-8 ，部分网站使用gbk
# str --- encode() --- bytes --- decode() --- str

