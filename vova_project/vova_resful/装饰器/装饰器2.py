import time

def deco(f):
    def wrapper(a,b):
        start_time = time.time()
        f(a,b)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" % execution_time)
    return wrapper

@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

if __name__ == '__main__':
    f(3,4)