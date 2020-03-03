#coding:utf-8
from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get(url)

driver.find_element_by_xpath('//*[@id="lg"]/img[200000]')