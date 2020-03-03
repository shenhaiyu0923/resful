from API2.lib.apiLib import *
import datetime,sys

tm = TeacherMgr()
#列出课程
listRetObj=tm.list_teacher(1,20)
listObj=listRetObj['retlist']
pprint(listObj)



