# -*- coding utf-8 -*-
# import subprocess
# #ret = subprocess.check_output(["ping", "www.baidu.com"])#阻塞式调用,不会返回状态码
# subprocess.Popen(["ping","www.baidu.com"])#非阻塞式调用,这是一个对象,想调用可以在下面加time.sleep(1)
# #subprocess.Popen(["ping","www.baidu.com"]).wait()#阻塞式调用
# print("123")
# #print(popen)
# #print(ret)
# #print("==================================")
import subprocess,time
# subprocess.Popen(["ping","www.baidu.com"])
# time.sleep(1)

a=subprocess.Popen(["ping","www.baidu.com"],
                 stdout=subprocess.PIPE,#管道
                 shell=True,
                 encoding='gbk'
                 )
output,err=a.communicate()#阻塞式调用
print(output)