def add1(x):
    return x+2

class TestABC():
    def test_add1(self):
        print('测试用例0001开始')
        assert add1(3)==4
        print('测试用例0001结束')

    def test_add2(self):
        print('测试用例0002开始')
        assert add1(3)==5
        print('测试用例0002结束')

#  pytest test_func.py
#  pytest -s test_func.py
#  pytest -s test_func.py
#pytest -s tc  --html=report1.html
