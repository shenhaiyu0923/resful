from pylib.Mobile_green import *

class Test_older3:
    def setup_method(self,):
        print('下单_tc0003 -- 初始化数据')
        pass
    def teardown_method(self,):
        print('下单_tc0003 -- 清除数据')
        pass

   # @badpng
    def test_green_0003(self):#用例一,信用卡下单验证
        ret=CardGreen.green_third('13121569', 'china')
        assert ret is not None
        print('\n 下单_tc0003 - 结束\n')

