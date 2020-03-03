import requests
import pprint
res=requests.get('http://www.baidu.com')
a=res.text
pprint.pprint(a)