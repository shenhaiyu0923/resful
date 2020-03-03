from API2.lib.apiLib import *
import datetime
import sys
#now_time = datetime.datetime.now()

cm = CourseMgr()#实例化

curTime = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())

courseName = f'py_{curTime}'

# 先列出课程
courseList1 = cm.list_course(1,20)['retlist']

# 先添加一个课程
addRetObj = cm.add_course(courseName,
                     'Python语言',
                     1)
assert addRetObj['retcode']==0

# 再删除课程
courseId=addRetObj['id']
delRetObj = cm.del_course(courseId)
print(delRetObj)  # 返回json格式的字符串
if delRetObj['retcode']==0:
    print("检查点===>返回结果retcode为0,删除成功")
else:
    print("检查点===>返回结果retcode不为0,删除失败")

print('\n ======== 用例002,执行通过 ======== \n')

