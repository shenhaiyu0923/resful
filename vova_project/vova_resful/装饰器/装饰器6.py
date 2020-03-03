from functools import wraps

def rau(func):
    @wraps(func)
    def inner_func():
        inner_obj = 'inner_obj'
        print(inner_obj)
        return func()
    return inner_func


@rau
def atest_func():
    return False

atest_func()

