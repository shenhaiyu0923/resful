#!/usr/bin/python
import json

data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
print(json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))
json = json.dumps(data,sort_keys=True, indent=6)
print(json)
print(data)


import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)

import time
print('='*70)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))





