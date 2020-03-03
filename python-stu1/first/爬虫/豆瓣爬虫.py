#  https://read.douban.com   豆瓣读书
#<div class="title"><a href="https://read.douban.com/column/31739013/?icn=from-author-page">我看见你杀了我</a><span class="label-category">连载</span></div>
import re
import urllib.request
#爬取以5开头的QQ号
data=urllib.request.urlopen("https://read.douban.com/author/63720083/").read()
data1=data.decode("utf-8")
pat='<div class="title">(.*?)</div>'
request=re.compile(pat).findall(str(data1))
fh=open('d://豆瓣.txt','w')
for i in range(0,len(request)):
    fh.write(request[i])
fh.close()
print(request)
