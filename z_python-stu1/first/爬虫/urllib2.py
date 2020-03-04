import re
import urllib.request
key="山东"
key=urllib.request.quote(key)
url='http://www,baidu.com/s?wd='+key+'ie=utf-8&tn=96542061_hao_pg'
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fh=open("d://bbb.html","w")
fh.write(data)
fh.close()

