from API2.lib.apiLib import *
import datetime
import sys
#now_time = datetime.datetime.now()

cm = CourseMgr()

curTime = '{0:%Y-%m-%d_%H:%M:%S}'.format(datetime.datetime.now())

courseName = f'py_{curTime}'

addRetObj=cm.add_course(courseName,'课程描述',12)
print(addRetObj)  # 返回json格式的字符串
if addRetObj['retcode']==0:
    print("检查点===>返回结果retcode为0,增加成功")
else:
    print("检查点===>返回结果retcode不为0,增加失败")
    sys.exit(1)

listRetObj = cm.list_course(1,20)
expected = {'desc':'课程描述' ,
              'display_idx': 12,
              'id': addRetObj['id'],
              'name': courseName}
if listRetObj['retlist'].count(expected)==1:
    print("检查点===>添加成功")
else:
    print("检查点===>添加失败")
    sys.exit(2)#让程序退出,推出码只要不等于0带表异常退出

print('\n ======== 用例001,执行通过 ======== \n')