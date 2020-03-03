from API2.lib.apiLib import *
import datetime
import sys

cm = CourseMgr()
#now_time = datetime.datetime.now()



# 先添加一个课程
curTime = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())
courseName = f'py_{curTime}'
addRetObj = cm.add_course(courseName,
                     'Python语言',
                     1)
assert addRetObj['retcode']==0

# 再修改课程
courseId = addRetObj['id']
newName = f"{courseName}_new"
updRetObj = cm.upd_course(courseId,
                     newName,
                     'Python语言',
                     1)
if updRetObj['retcode']==0:
    print("检查点===>返回结果retcode为0,修改成功")
else:
    print("检查点===>返回结果retcode不为0,修改失败")
    sys.exit(2)


courseList = cm.list_course(1,20)['retlist']
newCourse = None
for course in courseList:
    if course['id'] == courseId:
        newCourse = course


if newCourse['name'] == newName:
    print('===> 修改课程名成功，通过')
else:
    print('===> 修改课程名不成功，不通过！！！')
    sys.exit(2)
print('\n ======== 用例003,执行通过 ======== \n')

#列出课程
listRetObj=cm.list_course(1,20)
listObj=listRetObj['retlist']
pprint(listObj)