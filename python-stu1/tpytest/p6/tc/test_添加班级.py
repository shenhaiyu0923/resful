from p6.pylib.ApiSchoolClass import ins_ApiSchoolClass

class Test添加班级_tc000001:

    def teardown_method(self, method):
        print('用例添加班级_tc000001 -- 清除数据')

        ins_ApiSchoolClass.delete_school_class(self.classid)


    def test(self):
        print('\n 用例添加班级_tc000001 - 开始\n')

        print('添加班级')

        addRet = ins_ApiSchoolClass.add_school_class(1,
                                            '1班',
                                            60)

        self.classid = addRet['id']

        assert  addRet['retcode'] == 0


        print('列出班级')

        listRet = ins_ApiSchoolClass.list_school_class()

        expected = [
            {
                "name": "1班",
                "grade__name": "七年级",
                "invitecode": addRet['invitecode'],
                "studentlimit": 60,
                "studentnumber": 0,
                "id": addRet['id'],
                "teacherlist": []
            }
        ]

        assert listRet['retlist'] == expected


        print('\n 用例添加班级_tc000001 - 结束\n')
