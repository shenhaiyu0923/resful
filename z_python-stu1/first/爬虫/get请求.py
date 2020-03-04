import urllib.request
keywd1="山东"
#   https://www.baidu.com/s?wd=山东&tn=93733568_hao_pg
keywd=urllib.request.quote(keywd1)
url="http://www.baidu.com/s?wd="+keywd+"&ie=utf-8&tn=96542061_hao_pg"
req=urllib.request.Request(url)
data2=urllib.request.urlopen(req).read()
fh=open("D://abcd.html","wb")
fh.write(data2)
fh.close()


