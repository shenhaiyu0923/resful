# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/7/12

maxVar = 666

def foo():
    a = 99  # local 局部作用域
    def bar():
        b = 66 # enclosing 嵌套作用域
        def test():
            c = 77
        print(b)
    print(a)

foo()

# built-in
print(__name__)


