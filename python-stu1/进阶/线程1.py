import threading
from time import sleep

def thread1_entry():
    print('child thread 1,start')
    sleep(3)
    print('child thread 1,end')

t1=threading.Thread(target=thread1_entry())

t1.start()
sleep(5)
print('main thread end.')
