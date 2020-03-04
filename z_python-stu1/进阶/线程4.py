import threading
from time import sleep

#储存支付宝账号余额
zhifubao={
    'jcy':2000,
    'liming':5000
}
zhifubao_lock=threading.Lock()#设置锁

def thread1_didi_pay(account,amount):
    zhifubao_lock.acquire()#上锁
    print('*t1:get balance from bank')
    balance = zhifubao[account]
    print('*t1:do something1(like discount lookup)for 2 second')
    sleep(2)
    print('*t1:deduct')
    zhifubao[account]=balance - amount
    zhifubao_lock.release()#解锁
def thread1_yuebao_interest(account,amount):
    zhifubao_lock.acquire()
    print('*t1:get balance from bank')
    balance = zhifubao[account]
    print('*t1:do something2(like discount lookup)for 1 second')
    sleep(1)
    print('*t1:deduct')
    zhifubao[account]=balance + amount
    zhifubao_lock.release()
t1 = threading.Thread(target=thread1_didi_pay,args=('jcy',10))
t2 = threading.Thread(target=thread1_yuebao_interest,args=('jcy',10))
t1.start()#开启线程
t2.start()
t1.join()#等待线程结束
t2.join()

print('finally,jcy balance is %s' % zhifubao['jcy'])

