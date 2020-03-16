import pytest

# 函数级别，
# 每个测试函数前都会执行一次
# @pytest.fixture()
# def before():
#     print("在函数前执行")
#
# def test_a(before):
#     print("test_a在执行")
#
# def test_b(before):
#     print("test_b在执行")

# 作为装饰器执行
# @pytest.fixture()
# def before():
#     print("在函数前执行")
#
# @pytest.mark.usefixtures('before')
# def test_a():
#     print("test_a在执行")
#
# @pytest.mark.usefixtures('before')
# def test_b():
#     print("test_b在执行")
#
# @pytest.mark.usefixtures('before')
# class Test_ABC():
#     def test_c(self):
#         print("test_c在执行")
#
#     def test_d(self):
#         print("test_d在执行")

# 自动运行
# 作用域改为类， 类里面的每个函数只执行一次
# 但是类外边的函数每次都会调用before
# @pytest.fixture(scope="class", autouse=True)
# def before():
#     print("\n在函数前执行\n")
#
# @pytest.mark.usefixtures("before")
# def test_c():
#     print("\ntest_c在执行\n")
#
#
# @pytest.mark.usefixtures("before")
# def test_d():
#     print("\ntest_d在执行\n")
#
# class Test_ABC():
#     def test_a(self):
#         print("\ntest_a执行\n")
#
#     def test_b(self):
#         print("\ntest_b执行\n")

# 改为模块的使用
# 在模块中只执行一次，不管是否调用
# @pytest.fixture(scope="module", autouse=True)
# def before():
#     print("\n在函数前执行\n")
#
# @pytest.mark.usefixtures("before")
# def test_1():
#     print("\ntest1在执行")
#
# @pytest.mark.usefixtures("before")
# class Test_ABC():
#     def test_a(self):
#         print("\ntest_a在执行")
#
#     def test_b(self):
#         print("\ntest_b在执行")


# 使用param传递参数, 实现参数化
@pytest.fixture(params=[1, 2, 3])
def need_data(request): # 传入参数request 系统封装参数
      return request.param # 取列表中单个值，默认的取值方式

class Test_ABC():
    def test_a(self, need_data):
        print("test_a 的值是 %s" % need_data)



if __name__ == '__main__':
    pytest.main("test_fixture.py")




