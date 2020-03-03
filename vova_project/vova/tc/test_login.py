from pylib.MobileAdmin import *

class Test_login:
    def setup_method(self,):
        print('登陆用例_tc0001 -- 初始化数据')
        pass
    def teardown_method(self,):
        print('登陆用例_tc0001 -- 清除数据')
        pass

   # @badpng
    def test_login_0001(self):
        ret=login.email_login('p1210@tetx.com', '111111')
        #ret=login.email_login('t1213@163.com', '111111')
        assert ret == 'p1210'
        print('\n 登陆用例_tc0001 - 结束\n')

