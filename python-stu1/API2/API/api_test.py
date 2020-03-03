import requests
import pprint

# 3个参数，根据参数来发送相应的消息
#添加课程
def add_course(name,desc,displayidx):
    payload = {
        'action': 'add_course',
        # 格式化字符串的方式来构造消息
        'data':'''
        {
          "name":"%s",
          "desc":"%s",
          "display_idx":"%s"
        }''' % (name,desc,displayidx)

    }
    # data参数 就是构造消息体的
    response = requests.post("http://localhost/api/mgr/sq_mgr/",
                             data=payload)

    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)
    return retDict

#列出课程
def list_course():
    params = {
        'action':'list_course',
        'pagenum':'1',
        'pagesize':20
    }
    response = requests.get("http://localhost/api/mgr/sq_mgr/",
                            params=params)
    # 获取结果，返回给调用者
    retDict = response.json()
    pprint.pprint(retDict)

    # 获取结果，返回给调用者
    return retDict



# 先列出课程
coureListBefore = list_course()['retlist']
print("-------------------------1-----------------------------")
# 再添加一门课程
retDict = add_course('数学','数学描述1','2')
assert retDict['retcode'] == 0
print("-------------------------2-----------------------------")
# 再列出课程
coureListAfter = list_course()['retlist']

print("-------------------------3-----------------------------")
# 取出，多出来的一门课程对象
newcourse = None
for one in coureListAfter:
    if one not in coureListBefore:
        newcourse = one
        break


# 检查是否是刚刚添加的课程
assert newcourse!=None
assert newcourse['name']=='数学'
assert newcourse['desc']=='数学描述'
assert newcourse['display_idx']==2

print('\n========= test case pass =============')
