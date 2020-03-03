#coding:utf-8
from selenium import webdriver
# selenium 1.0  selenium
# selenium 2.0  webdriver + selenium
# selneium 3.0  webdriver

# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get('http://www.baidu.com')

# 2.定位元素
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python37')
driver.find_element_by_xpath('//*[@id="su"]').click()