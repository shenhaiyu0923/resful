import requests


# /api/mgr/sq_mgr/
def listTeacher():
    params={'action':'list_teacher', 'pagenum':'1', 'pagesize':20 }
    response=requests.get("http://localhost/api/mgr/sq_mgr/",params=params)
    bodyDict=response.json()
    print(bodyDict)
    return bodyDict
    #return [one['name'] for one in  bodyDict['retlist']]

if '__main__'==__name__:
    cnamelist=listTeacher()
    for one in cnamelist:
        print(one)
