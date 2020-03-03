#!/usr/bin/env python3   第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*-   第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

a =ord('A')    #查询字符编码
print(a)
print(ord('A'))
ord('中')
chr(66)   #将字符编码转换成字符串
print(chr(66))   #B
chr(25991)
print(chr(25991))  #文

'中文'.encode('utf-8')  #b'\xe4\xb8\xad\xe6\x96\x87'   将字符串转换成字节
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')     #'中文'从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')      #'中'   排除部分无效字节
len('ABC')   #3    查询字符数
