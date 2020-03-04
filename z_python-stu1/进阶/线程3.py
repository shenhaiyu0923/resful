import threading
from time import sleep

def thread_entry():
    var=1#局部变量
    for i in range(5):
        print('th #{}:{}'.format(threading.currentThread().ident,var))
        sleep(1)
        var +=1

print('main thread start')
t1 = threading.Thread(target=thread_entry)
t2 = threading.Thread(target=thread_entry)
t1.start()#开启线程
t2.start()
t1.join()#等待线程结束
t2.join()
print('main thread end.')
