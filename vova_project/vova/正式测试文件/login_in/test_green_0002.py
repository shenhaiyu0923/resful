from pylib.Mobile_green import *

class Test_older2:
    def setup_method(self,):
        print('下单_tc0002 -- 初始化数据')
        pass
    def teardown_method(self,):
        print('下单_tc0002 -- 清除数据')
        pass

   # @badpng
    def test_green_0002(self):#用例一,信用卡下单验证
        ret=CardGreen.green_second('1090423', 'china')
        assert ret is not None
        print('\n 下单_tc0002 - 结束\n')

