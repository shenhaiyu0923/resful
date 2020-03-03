import pytest
from pylib.MobileAdmin import *
@pytest.fixture(scope='package',autouse=True)#fixture是测试装置，package声明对当前目录下所有包有效，autouse声明自动使用

def st_clearAll(request):
    print(f'\n---初始化：：构建空白数据环境')
    d.click_post_delay = 1  # 设置每次单击UI并单击后的延迟0.5s
    d.wait_timeout = 30.0  # ＃设置默认元素等待超时（秒）
    d.app_clear(vova_android)
    d.session(vova_android)
    #self.d.app_start(vova_android)
    def fin():
        print(f'\n---清除：：清除空白数据环境')
        #self.d.app_clear(vova_android)
    request.addfinalizer(fin)