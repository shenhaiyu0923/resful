import requests




def listCourse1():
    params={'action':'list_course', 'pagenum':'1', 'pagesize':20 }
    response=requests.get("http://localhost/api/mgr/sq_mgr/",params=params)
    bodyDict=response.json()
    print(bodyDict)
    return [one['name'] for one in  bodyDict['retlist']]



if '__main__'==__name__:
    cnamelist=listCourse1()
    for one in cnamelist:
        print(one)
