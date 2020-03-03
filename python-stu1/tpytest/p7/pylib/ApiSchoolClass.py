import requests
from p7.cfg import *
from pprint import pprint


class ApiSchoolClass:

    def list_school_class(self,gradeid=None):

        params = {
            'vcode' : g_vcode,
            'action' : 'list_classes_by_schoolgrade'
        }


        if gradeid != None:
            params['gradeid'] = gradeid

        response = requests.get(g_api_schoolclass_path,
                     params=params)

        body = response.json()
        pprint(body)

        return body


    def add_school_class(self,gradeid,name,studentlimit):

        payload = {
            'vcode' : g_vcode,
            'action' : 'add',
            'grade' : gradeid,
            'name' : name,
            'studentlimit' : studentlimit,
        }


        response = requests.post(g_api_schoolclass_path,
                     data=payload)

        body = response.json()
        pprint(body)

        return body




    def delete_school_class(self,classid):

        payload = {
            'vcode' : g_vcode,
        }

        url = f'{g_api_schoolclass_path}/{classid}'

        response = requests.delete(url,
                     data=payload)

        body = response.json()
        pprint(body)

        return body


    def delete_all_school_class(self):

        rd = self.list_school_class()

        for sc in rd["retlist"]:
            cid = sc["id"]
            self.delete_school_class(cid)

        return


ins_ApiSchoolClass = ApiSchoolClass()