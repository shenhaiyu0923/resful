import pytest
from pylib.MobileAdmin import *
@pytest.fixture(scope='package',autouse=True)#fixture是测试装置，package声明对当前目录下所有包有效，autouse声明自动使用
def st_clearAll(request):
    print(f'\n---初始化：：信用卡下单环境')
    def fin():
        pass
        #self.d.app_clear(vova_android)
    request.addfinalizer(fin)