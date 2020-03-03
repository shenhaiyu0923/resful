import requests
from p5.cfg import *

from pprint import pprint
import json


class ApiTeacher:

    def list_teacher(self,subjectid=None):

        params = {
            'vcode' : g_vcode,
            'action' : 'search_with_pagenation'
        }


        if subjectid != None:
            params['subjectid'] = subjectid

        response = requests.get(g_api_teacher_path,
                     params=params)

        body = response.json()
        pprint(body)

        return body


    def add_teacher(self,
                    username,
                    realname,
                    subjectid,
                    classlist,
                    phonenumber,
                    email,
                    idcardnumber):

        payload = {
            'vcode' : g_vcode,
            'action' : 'add',
            'username' : username,
            'realname' : realname,
            'subjectid' : subjectid,
            'classlist' : json.dumps(classlist),
            'phonenumber' : phonenumber,
            'email' : email,
            'idcardnumber' : idcardnumber,
        }


        response = requests.post(g_api_teacher_path,
                     data=payload)

        body = response.json()
        pprint(body)

        return body




    def delete_teacher(self,teacherid):

        payload = {
            'vcode' : g_vcode,
        }

        url = f'{g_api_teacher_path}/{teacherid}'

        response = requests.delete(url,
                     data=payload)

        body = response.json()
        pprint(body)

        return body


    def delete_all_teacher(self):

        rd = self.list_teacher()

        for sc in rd["retlist"]:
            cid = sc["id"]
            self.delete_teacher(cid)

        return


ins_ApiTeacher = ApiTeacher()