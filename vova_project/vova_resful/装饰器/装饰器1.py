import time

def deco(fun):
    def wrapper():
        start_time = time.time()
        fun()
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def f():
    print("hello")
    time.sleep(2)
    print("world")

if __name__ == '__main__':
    f()