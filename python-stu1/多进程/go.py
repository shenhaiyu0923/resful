
from ctypes import CDLL
# 无参数，则可直接调用
t = CDLL('F:/dog/fit.so').test #调用ｇｏ模块
print(t(65535))

i=0
sum=0

while i<67000:
    i+=1
    sum=sum+i

print(sum)
