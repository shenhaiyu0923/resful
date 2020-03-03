import requests

url = "http://www.baidu.com/"

response = requests.get(url)

print(response)  #<Response [200]>
print(response.url)#http://www.baidu.com/
print(response.status_code)#200 状态码
print(response.request.headers)#请求头
print(response.headers)#响应头
print(response.request._cookies)# <RequestsCookieJar[]>
print(response.cookies)#<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(response.encoding)#输出默认编码格式：ISO-8859-1
response.encoding = "utf8" #指定编码格式
print(response.encoding)# utf8
print(response.text) #如果不声明指定编码格式utf8，就会以默认编码格式输出（不识别中文）
print(response.encoding)
print(response.content.decode())#==比response.text适用中文

#print(response.json())#如果是json，可以以json打印输出