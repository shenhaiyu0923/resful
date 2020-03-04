import requests
from API2.cfg import API_SERVER
from API2.lib import apiLib
import datetime
from pprint import pprint
import sys
#now_time = datetime.datetime.now()
curTime = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())

courseName = f'py_{curTime}'

retObj,sessionid=apiLib.login('auto','sdfsdfsdf')


AddretObj=apiLib.add_course(courseName,'课程描述',12)
print(AddretObj)  # 返回json格式的字符串
if AddretObj['retcode']==0:
    print("检查点===>返回结果retcode为0,增加成功")
else:
    print("检查点===>返回结果retcode不为0,增加失败")


listRetObj=apiLib.list_course(1,20)
listObj=listRetObj['retlist']
pprint(listObj)

