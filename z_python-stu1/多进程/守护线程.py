import threading
import time

def tstart(arg):
    print("%s running....at: %s" % (arg,time.time()))
    time.sleep(1)
    print("%s is finished! at: %s" % (arg,time.time()))

if __name__ == '__main__':
    t1 = threading.Thread(target=tstart, args=('This is thread 1',))
    t1.setDaemon(True)
    t1.start()
   # t1.join()   # 当前线程阻塞，等待t1线程执行完成
    print("This is main function at：%s" % time.time())
