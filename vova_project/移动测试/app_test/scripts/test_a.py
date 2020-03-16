import pytest


def test_a():
    hello_a()

# 定义的函数必须以test开头
def hello_a():
    print("***"*10)
    assert 1