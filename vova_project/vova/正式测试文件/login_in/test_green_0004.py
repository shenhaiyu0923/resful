from pylib.Mobile_green import *

class Test_older:
    def setup_method(self,):
        print('下单_tc0004 -- 初始化数据')
        pass
    def teardown_method(self,):
        print('下单_tc0004 -- 清除数据')
        pass

   # @badpng
    def test_green_0004(self):#用例一,信用卡下单验证
        ret=CardGreen.green_fourth('13121569', 'Poland')
        print('\n 下单_tc0004 - 结束\n')

