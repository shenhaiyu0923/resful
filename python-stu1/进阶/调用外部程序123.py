import os
os.system('qq')#打开绘图工具,阻塞式请求
os.system('mspaint')#打开绘图工具,阻塞式请求
os.system('mspaint e:/132.png')#打开指定图片,阻塞式请求
print("after call")
ret=os.system("dir")
if ret==0:
    print("123你好")
else:
    print("4324你好")

os.system('')







