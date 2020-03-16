import pytest

# 修该函数的执行顺序
# 都是正数的话，值越小越先执行
# 都是负数的话，值越小越先执行
# 0和负数的话，0先执行，剩下的值越小越先执行
# 0和正数， 0先执行，剩下的值越小越先执行
# 0和负数和正数， 0先执行正数接着负数最后
# 总结： 0 》 较小的正数 》较大的正数 》 较小的负数 》 较大的负数
@pytest.mark.run(order=0)
def test_a():
    print("\ntest_a-----》")
    assert 1
@pytest.mark.run(order=2)
def test_b():
    print("\ntest_b")
    assert 0
@pytest.mark.run(order=-4)
def test_hello():
    print("\nhello_test")
    assert 1

if __name__ == '__main__':
    pytest.main("test_hello.py")



