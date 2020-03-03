import urllib.request
import re
data=urllib.request.urlopen("https://news.sina.com.cn/").read().decode("utf-8","ignore")
pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data)
print(allurl)
for i in range(0,len(allurl)):
    try:
        thisurl=allurl[i]
        file="D:/xinlang/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("…………第"+str(i)+"次成功…………")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

