from p9.pylib.ApiTeacher import  ins_ApiTeacher
from p9.pylib.ApiTeacher import  ins_ApiTeacher
from p9.pylib.ApiSchoolClass import ins_ApiSchoolClass
from p9.pylib.MobileAdmin import ins_MobileAdmin

class Test添加老师_tc001001:

    def teardown_method(self, method):
        print('用例添加老师_tc001001 -- 清除数据')

        ins_ApiTeacher.delete_teacher(self.tid)

    def test(self,st_g7c1):
        print('\n 用例添加老师_tc001001 - 开始\n')

        print('添加老师')

        classid = st_g7c1['id']
        addRet = ins_ApiTeacher.add_teacher(
                'tuobaliwei',
                '拓跋力威',
                1,
                [{'id':classid}],
            '13110000001', '13110000001@g.com', '13110000001'
                )

        self.tid = addRet['id']

        assert  addRet['retcode'] == 0

        print('列出老师')

        listRet = ins_ApiTeacher.list_teacher()

        expected = [{
            "username": "tuobaliwei",
            "realname": "拓跋力威",
            "id": addRet['id'],
            "phonenumber": "13110000001",
            "email": "13110000001@g.com",
            "idcardnumber": "13110000001",
            "teachclasslist": [classid],
        },
]

        assert expected == listRet['retlist']


        print('\n 用例添加老师_tc001001 - 结束\n')
