# -*- coding: utf-8 -*-
import time

def calu(tps):
    def bar(func):
        def inner(*args, **kwargs):
            begin = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("值 =", tps/(end - begin))

        return inner
    return bar

@calu(100)  # foo = calu(100)
def foo(user, a):
    print("执行者：%s 执行了测试用例" % user)
    print(a)
    time.sleep(1)

foo("王五", [1, 45, 7])




