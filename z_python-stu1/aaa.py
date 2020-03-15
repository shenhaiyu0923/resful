#!/usr/bin/python
import json

data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }

for num ,d in enumerate(data):
    print(str(num)+"="+str(d))


data='a=1;b=2;c=3'
#cookies = {cookie.split('=')[0]:cookie.split('=')[1]for cookie in cookie_list}
list={a.split('=')[0]:a.split('=')[1] for a in data.split(';')}
print(list)

