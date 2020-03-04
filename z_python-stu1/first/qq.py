#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : QQ轰炸.py
# @Author: 未衬


'''
通过python去控制键盘和鼠标
'''

# 导入响应的库 pip install pynput
import time

# 键盘控制器 必须带上别名
from pynput.keyboard import Controller as key_cl

# 鼠标控制器
from pynput.mouse import Button, Controller


# 键盘控制函数
def keyboard_input(string):
    keyboard = key_cl()
    keyboard.type(string)


# 鼠标控制函数
def mouse_click():
    mouse = Controller()
    mouse.press(Button.left)
    mouse.release(Button.left)

# 执行函数
def main(number, string):
    time.sleep(7)
    for i in range(number):
        keyboard_input(string)
        mouse_click()
        time.sleep(0.2)

# 程序执行入口
if __name__ == "__main__":
    main(5, '派森牛批')
