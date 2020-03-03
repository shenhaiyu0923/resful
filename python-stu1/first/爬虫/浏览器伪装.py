import urllib.request
import re
url='https://read.douban.com/author/63720083/'
headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
#不支持高级报头，所以用下面这个
opener=urllib.request.build_opener()  #创建opener对象
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
pat='<div class="title"><a href="(https.*?)"'
allurl=re.compile(pat).findall(data)
print(allurl)#此处获取到5个URL，下面的代码存储成5个html时出错了
for i in range(0,len(allurl)):
    thisurl = allurl[i]
    file ="D:/xinlang/"+str(i)+".html"
    urllib.request.urlretrieve(thisurl,file)
    print("…………第"+str(i)+"次成功…………")
