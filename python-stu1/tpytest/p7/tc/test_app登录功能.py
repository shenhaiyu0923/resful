from p7.pylib.WebTeacher import ins_WebTeacher
from p7.pylib.ApiTeacher import ins_ApiTeacher
from p7.pylib.ApiSchoolClass import ins_ApiSchoolClass
from p7.pylib.MobileAdmin import ins_MobileAdmin
class Test_vcode登录_tc006001:
    def teardown_method(self, method):
        print('用例vcode登录_tc006001 -- 清除环境')

        ins_MobileAdmin.close_mobile()

    def test(self):
        print('\n 用例vcode登录_tc006001 - 开始\n')

        print('使用错误的vcode登录')

        ret = ins_MobileAdmin.open_mobile()

        ret = ins_MobileAdmin.vcode_login('23423223')

        assert  ret == {'ret':False, 'info':'登录失败 : vcode format error:1'}


        print('\n 用例vcode登录_tc006001 - 结束\n')
