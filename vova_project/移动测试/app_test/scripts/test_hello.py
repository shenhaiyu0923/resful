import pytest

# 定义的函数必须以test开头
def test_a():
    print("\ntest_a")
    assert 1


def test_b():
    print("\ntest_b")
    assert 0

def test_hello():
    print("\nhello_test")
    assert 1

if __name__ == '__main__':
    pytest.main("-s test_hello.py")



