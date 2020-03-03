# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/7/12



def foo():
    b = 99
    def inner():
        print(b)
    return inner

a = foo()

a()

foo()()