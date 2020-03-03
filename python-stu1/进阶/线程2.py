import threading
from time import sleep,ctime

def thread1_entry(nsec):
    print('child thread 1,start',ctime())
    sleep(nsec)
    print('child thread 1,end',ctime())

def thread2_entry(nsec):
    print('child thread 2,start',ctime())
    sleep(nsec)
    print('child thread 2,end',ctime())

if __name__=='__main__':
    print('main thread start.')
    t1 = threading.Thread(target=thread1_entry,args=(1,))#thread1_entry函数对象
    #t1 = threading.Thread(target=thread1_entry(1),args=(1,))#thread1_entry(1)函数调用的返回值
    t2 = threading.Thread(target=thread2_entry,args=(1,))
    t1.start()#开启线程
    t2.start()
    t1.join()#等待线程结束
    t2.join()
    sleep(5)
    print('main thread end.')
