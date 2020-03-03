import requests
#from work888.cfg import API_SERVER
from pprint import pprint
import json
import sys


class test8():
    #增加课程
    def add_course(self,name, desc, display_idx):
        data = {
            'action': "add_course",
            'data': f'''
            {{
                "name":"{name}",
                "desc":"{desc}",
                "display_idx":"{display_idx}"
            }}
            '''
        }
        res = requests.post(f'http://localhost/api/mgr/sq_mgr/', data=data)
        AddretObj = res.json()
        return AddretObj


    #删除课程
    def del_course(self,id):
        data = {
            "action": "delete_course",
            "id": id
                }

        res = requests.delete(f'http://localhost/api/mgr/sq_mgr/',data=data)
        print(res)
        retObj = res.json()
        return retObj


    #列出课程
    def list_course(self):
        params = {
            "action": "list_course",
            "pagenum": 1,
            "pagesize": 20
                  }

        res = requests.get(f'http://localhost/api/mgr/sq_mgr/',params=params)
        retObj = res.json()
       # pprint(retObj, width=60)
        return retObj

    #增加老师
    def add_teacher(self,username,password,realname,desc,courses,display_idx):
        data = {
            'action': "add_teacher",
            'data': f'''
            {{
                "username":"{username}",
                "password":"{password}",
                "realname":"{realname}",
                "desc":"{desc}",
                "courses":{json.dumps(courses)},
                "display_idx":"{display_idx}"
            }}
            '''
        }
        res = requests.post(f'http://localhost/api/mgr/sq_mgr/',data=data)
        AddretObj = res.json()
        return AddretObj

    def del_teacher(self,id):
        data = {
            "action": "delete_teacher",
            "id": id
                }

        res = requests.delete(f'http://localhost/api/mgr/sq_mgr/',data=data)
        retObj = res.json()
        pprint(retObj,width=60)
        return retObj

    #列出老师
    def list_teacher(self):
        params = {
            "action": "list_teacher",
            "pagenum": 1,
            "pagesize": 20
        }
        res = requests.get(f'http://localhost/api/mgr/sq_mgr/', params=params)
        retObj = res.json()
        #pprint(retObj, width=60)
        return retObj


    '''
    
    print('=========================增加课程====================================')
    addRetObj=add_course('数学','数学描述',1)
    print(addRetObj)  # 返回json格式的字符串
    if addRetObj['retcode']==0:
        print("检查点===>返回结果retcode为0,增加成功")
    else:
        print("检查点===>返回结果retcode不为0,增加失败")
        #sys.exit(1)
    
    
    
    print('========================列出课程=====================================')
    
    listRetObj=list_course()
    listObj=listRetObj['retlist']
    pprint(listObj)
    
    
    
    print('========================增加老师=====================================')
    addTeacherRet=add_teacher(
        '周扬',
        'zyz111',
        'tesch',
        'tesch src',
        [{"id":addRetObj['id'],"name":'数学'}],
        1
    )
    print(addTeacherRet)
    if addTeacherRet['retcode'] == 0:
        print('===> 添加老师返回结果retcode为0，通过')
    else:
        print('===> 添加老师返回结果retcode不为0，不通过！！！')
        #sys.exit(1)
    
    
    print('========================列出老师=====================================')
    
    listRetObj=list_teacher()
    listObj=listRetObj['retlist']
    pprint(listObj)
    
    
    print('========================删除老师=====================================')
    teacherId = addTeacherRet['id']
    delRetObj = del_teacher(teacherId)
    print(delRetObj)  # 返回json格式的字符串
    if delRetObj['retcode'] == 0:
        print("检查点===>返回结果retcode为0,删除成功")
    else:
        print("检查点===>返回结果retcode不为0,删除失败")
    
    
    
    print('========================删除课程====================================')
    
    courseId=addRetObj['id']
    delRetObj = del_course(courseId)
    print(delRetObj)  # 返回json格式的字符串
    if delRetObj['retcode']==0:
        print("检查点===>返回结果retcode为0,删除成功")
    else:
        print("检查点===>返回结果retcode不为0,删除失败")
    
    
'''