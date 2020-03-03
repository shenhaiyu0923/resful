import functools

def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if not text is None:
                print(text)
            print('begin call')
            result=func(*args, **kw)
            print('end call')
            return result
        return wrapper
    return decorator

@log('hello')
def now(x,y):
    print(x+y)
    return x+y
now(1,2)