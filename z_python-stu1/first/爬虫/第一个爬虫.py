import re
import urllib.request
#爬取以5开头的QQ号
pat="<p>(5.*?)</p>"
data=urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/215").read()
request=re.compile(pat).findall(str(data))
print(request)
