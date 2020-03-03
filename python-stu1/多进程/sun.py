#!/usr/bin/env python
from ctypes import CDLL

lib = CDLL('F:/dog/main.so')
print(lib.Sum(7, 11))