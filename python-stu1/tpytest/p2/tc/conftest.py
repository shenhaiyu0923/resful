import pytest

@pytest.fixture(scope='package',autouse=True)#fixture是测试装置，package声明对当前目录下所有包有效，autouse声明自动使用
def st_clearAll(request):
    print(f'\n---初始化：：构建空白数据环境')
    def fin():
        print(f'\n---清除：：清除空白数据环境')
    request.addfinalizer(fin)

#  pytest -s tc  --html=report1.html