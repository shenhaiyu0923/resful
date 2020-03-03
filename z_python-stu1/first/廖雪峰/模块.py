import urllib
from urllib.request import urlopen
import request
a=urllib.request.urlopen('https://www.baidu.com').read()
print(len(a))
a1=urlopen('http://m.baidu.com').read()
print(len(a1))
from  urllib import  request
a2=request.urlopen('http://jd.com').read()
print(len(a2))