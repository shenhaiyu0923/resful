import requests
import pprint

payload={
    "action":"list_course",
    "pagenum":"1",
    "pagesize":"20"
}
r=requests.get('http://efrs.icbc.com.cn/icbc/efrsnew/ctrl/admin/queryUser',
               data=payload)
print(r.status_code)#打印状态码
print(r.headers)#打印响应头,可以看到是json格式
pprint.pprint(r.json())
pprint.pprint(dict(r.headers))



