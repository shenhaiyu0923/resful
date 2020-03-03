import win32com.client
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://tinypng.com/")
driver.find_element_by_css_selector('.icon').click()
#获取shell对象
shell = win32com.client.Dispatch("WScript.Shell")
time.sleep(3)
#使用shell对象的Sendkeys方法给应用程序发送字符串
shell.Sendkeys(r"C:\study\1234.png" + '\n')
print("=========================")
