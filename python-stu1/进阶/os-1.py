# import os
#
# os.system("ping www.baidu.com")
#
# print("after")

import subprocess, time

out_bytes = subprocess.check_output(["ping", "www.baidu.com"])#subprocess函数不会直接打印
out_bytes1 = subprocess.check_output(["pip","list"])
print(out_bytes.decode("gbk"))
print(out_bytes1.decode("gbk"))
#subprocess.Popen(["ping", "www.baidu.com"])   #popen函数直接会打印