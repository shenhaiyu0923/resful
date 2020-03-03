import urllib.request
import re
keyname="长裙"
key=urllib.request.quote(keyname)
#headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0')#火狐请求头
headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
opener=urllib.request.build_opener()  #创建opener对象
opener.addheaders=[headers]
urllib.request.install_opener(opener)#全局对象
for i in range(0,3):
    url = "http://s.taobao.com/search?q="+key+"&imgfile=&commend=all&ssid=s5-e&search_type=" \
    "item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&" \
     "bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s="+str(i*22)
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    pat='pic_url":"//(.*?)"'
    imagelist=re.compile(pat).findall(data)
    print(imagelist)
    for j in range(0,len(imagelist)):
        thisimg=imagelist[j]
        thisimgurl="http://"+thisimg
        file="d:/taobao/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl,file)
