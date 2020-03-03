from pylib.Mobile_green import *

class Test_older1:
    def setup_method(self,):
        print('下单_tc0001 -- 初始化数据')
        pass
    def teardown_method(self,):
        print('下单_tc0001 -- 清除数据')
        pass

   # @badpng
    def test_green_0001(self):#用例一,信用卡下单验证
        ret=CardGreen.green_first('13121566', 'china')
        assert ret is not None
        print('\n 下单_tc0001 - 结束\n')

