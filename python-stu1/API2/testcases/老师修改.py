from API2.lib.apiLib import *
import datetime,sys

cm = CourseMgr()

retObj,sessionid = cm.login('auto','sdfsdfsdf')

curTime = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())

courseName = f'python_{curTime}'


# 先添加一个课程
addRetObj = cm.add_course(courseName,
                     'Python语言',
                     1)

assert addRetObj['retcode'] == 0

courseId = addRetObj['id']

# 再添加老师
tm = TeacherMgr(sessionid)

teachername =   f'zyz_{curTime}'
addTeacherRet = tm.add_teacher(
    teachername,
    'zyz111',
    '朱元璋',
    '朱元璋，太残忍',
    [{"id":courseId,"name":courseName}],
    1
)
assert addTeacherRet['retcode']==0

# 再修改老师
teacherId=addTeacherRet['id']
newName = f"{teachername}_new"
updRetObj = tm.upd_teacher(teacherId,
                           "lishiming",
                           "sq888",
                           "李世民",
                           "李世民老师",
                           [{"id": courseId, "name": courseName}],
                           1)
if updRetObj['retcode']==0:
    print("检查点===>返回结果retcode为0,修改成功")
else:
    print("检查点===>返回结果retcode不为0,修改失败")
    sys.exit(2)

print('\n ======== 用例011,执行通过 ======== \n')