from p7.pylib.WebTeacher import ins_WebTeacher
from p7.pylib.ApiTeacher import ins_ApiTeacher
class Test老师登录_tc005001:

    def teardown_method(self, method):
        print('用例添加老师_tc005001 -- 清除数据')

        ins_ApiTeacher.delete_teacher(self.tid)

    def test(self,st_g7c1):
        print('\n 用例 老师登录_tc005001 - 开始\n')

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


        ins_WebTeacher.teacher_login(
            'tuobaliwei',
            '888888'
        )


        homepageinfo = ins_WebTeacher.get_teacher_homepage_info()

        assert  homepageinfo == [
            '松勤学院00677',
            '拓跋力威',
            '初中数学',
            '0',
            '0',
            '0',
        ]

        studentsinfo = ins_WebTeacher.get_teacher_class_students_info()

        assert  studentsinfo == {
            '七年级1班':[]
        }


        print('\n 用例 老师登录_tc005001 - 结束\n')
