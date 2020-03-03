# coding:utf-8
import os,time
import uiautomator2 as u2
from functools import wraps

curtime=time.strftime("%Y%m%d-%H%M%S", time.localtime())

def deviceslist():
    # popen返回文件对象，跟open操作一样
    f = os.popen(r"adb devices", "r")
    shuchu = f.read()
    f.close()
    #print(shuchu)  # cmd输出结果

    # 输出结果字符串处理
    s = shuchu.split("\n")   # 切割换行
    new = [x for x in s if x != '']  # 去掉空''
    #print(new)
    # 可能有多个手机设备
    devices = []  # 获取设备名称
    for i in new:
        dev = i.split('\tdevice')
        if len(dev)>=2:
            devices.append(dev[0])
    if not devices:
        print("手机没连上")
    else:
        print("当前手机设备:%s"%str(devices))
        return devices[0]


def badpng(func):#出错时截图装饰器
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            func(*args, **kwargs)
        except:
            curtime = time.strftime("%Y%m%d-%H%M%S", time.localtime())
            d.screenshot('image\{}.png'.format(func.__name__+'_'+curtime))
            print("异常函数:"+func.__name__+'_'+curtime)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print("time is %d ms" % execution_time)
    return wrapper

#feeec6d8
#devices_id=deviceslist()
#d = u2.connect(devices_id)

d = u2.connect('feeec6d8')
vova_android = 'com.vova.android'   #设备
vova_android = 'com.vova.android'   #设备
