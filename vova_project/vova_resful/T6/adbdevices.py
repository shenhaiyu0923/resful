# coding:utf-8
import os

# popen返回文件对象，跟open操作一样
f = os.popen(r"adb devices", "r")
shuchu = f.read()
f.close()

print(shuchu)  # cmd输出结果

# 输出结果字符串处理
s = shuchu.split("\n")   # 切割换行
new = [x for x in s if x != '']  # 去掉空''
print(new)


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