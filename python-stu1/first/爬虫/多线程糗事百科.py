import threading  #多线程
import urllib.request
import re
import urllib.error
headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
opener=urllib.request.build_opener()  #创建opener对象
opener.addheaders=[headers]
urllib.request.install_opener(opener)#全局对象
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,13,2):
            url = 'https://www.qiushibaike.com/hot/page/' + str(i)
            pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datelist = re.compile(pat, re.S).findall(pagedata)  # re.S 多行修正符
            print(datelist)
            for j in range(0, len(datelist)):
                print('第' + str(i) + '页第' + str(j) + '个段子的内容是')
                print(datelist[j])
class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,13,2):
            url = 'https://www.qiushibaike.com/hot/page/' + str(i)
            pagedata = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datelist = re.compile(pat, re.S).findall(pagedata)  # re.S 多行修正符
            print(datelist)
            for j in range(0, len(datelist)):
                print('第' + str(i) + '页第' + str(j) + '个段子的内容是')
                print(datelist[j])
t1=One()
t1.start()
t2=Two()
t2.start()













