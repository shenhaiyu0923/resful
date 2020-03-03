import urllib.request
import re
allurl=['https://read.douban.com/column/31739013/?icn=from-author-page', 'https://read.douban.com/column/31434748/?icn=from-author-page', 'https://read.douban.com/column/31434748/?icn=from-author-page', 'https://read.douban.com/column/31739013/?icn=from-author-page', 'https://read.douban.com/column/7444162/?icn=from-author-page']
for i in range(0,len(allurl)):
        thisurl=allurl[i]
        file="D:/xinlang/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("…………第"+str(i)+"次成功…………")
