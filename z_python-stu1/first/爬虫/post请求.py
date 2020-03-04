import urllib.request
import urllib.parse
url="https://www.iqianyue.com/mypost/"
data1=urllib.parse.urlencode({
"name":"wangjian.@qq.com",
"pass":"mima.@qq.com"
}).encode("utf-8")
req=urllib.request.Request(url,data1)
data2=urllib.request.urlopen(req).read()
fh=open("D://abc.html","wb")
fh.write(data2)
fh.close()







