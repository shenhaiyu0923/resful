# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/7/12


# # import os
# #
# # os.system("ping www.baidu.com")
# #
# # print("after")
#
# import subprocess, time
#
# # out_bytes = subprocess.check_output(["ping", "www.baidu.com"])
# #
# # print(out_bytes.decode("gbk"))
#
# subprocess.Popen(["ping", "www.baidu.com"])

import subprocess,time
a = subprocess.Popen(
        "python ioTest.py",#这个路径没有设置成绝对路径,报错了
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        encoding="gbk"
)
list = ['1','2','3','4']
output,err = a.communicate('\n'.join(list))
print("=====================================")
print(output)
print("=====================================")


