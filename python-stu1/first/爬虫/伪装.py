import urllib.request
import re
url='https://read.douban.com/author/63720083/'
headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
#不支持高级报头，所以用下面这个
opener=urllib.request.build_opener()  #创建opener对象
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open("d:/weizhuang/4.html","wb")
fh.write(data)
fh.close()



'''
pat='<div class="title">(.*?)</div>'
result=re.compile(pat).findall(data)
for i in range(0,len(result)):
    file ="D:/weizhuang/"+str[i]+".html"
    urllib.request.urlretrieve(result[i],filename=file)
    print("第"+str[i]+"次爬取成功")
'''


