# coding:utf8
from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://baidu.com')
print(driver.title)

driver.find_element_by_id('kw').send_keys('松勤\n')
time.sleep(3)
print(driver.title)
print(driver.current_url)#当前url

assert driver.title=='松勤_百度搜索'  #断言
driver.quit()