from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('http://baidu.com')
driver.get_screenshot_as_file('baidu.png')
#driver.get_screenshot_as_file('d:/baidu.png')
print('=============================')
driver.quit()