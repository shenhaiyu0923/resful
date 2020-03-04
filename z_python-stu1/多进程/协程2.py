#!/usr/bin/env python
# -*- coding:utf-8 -*-
from greenlet import greenlet
def taest1():
    print (11)
    gr2.switch()    #手动切换
    print (22)
    gr2.switch()

def taest2():
    print (33)
    gr1.switch()
    print (44)

gr1 = greenlet(taest1)
gr2 = greenlet(taest2)
gr1.switch()