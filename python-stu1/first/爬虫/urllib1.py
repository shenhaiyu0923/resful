import urllib.request
#urllib.request.urlretrieve('https://www.hellobi.com/',filename='d:/aaa.html') #此方法可以直接爬到本地
#urllib.request.urlcleanup()  #清除缓存
'''
file=urllib.request.urlopen('https://www.hellobi.com')
a2=file.info()   #环境信息
print(a2)
a1=file.getcode()  #200  状态码
print(a1)
a=file.geturl()   #https://www.hellobi.com/
print(a)
#超时 设置超时
file=urllib.request.urlopen('https://www.hellobi.com',timeout=0.1)  #设置为0.1秒，超出0.1秒为超时
'''
for i in range(0,20):
    try:
        file = urllib.request.urlopen('https://www.hellobi.com', timeout=0.2)
        data=file.read()
        print(len(data))
    except Exception as e:
        print('出现异常'+str(e))