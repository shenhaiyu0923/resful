import time
from functools import wraps
def deco01(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("this is deco01")
        start_time = time.time()
        try:
            func(*args, **kwargs)
        except:
            print(123)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
        print("deco01 end here")
    return wrapper


@deco01
def fuma(a,b):
    print(a+b)
    result=a+b
    assert result==5
fuma(2,4)
