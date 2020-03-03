#coding:utf-8
from selenium import webdriver


url = 'https://qzone.qq.com/'

driver = webdriver.Chrome()

driver.get(url)

el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
# driver.switch_to.frame('login_frame')
driver.switch_to.frame(el_frame)


driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1802161998')
driver.find_element_by_id('p').send_keys('guiji923')
driver.find_element_by_id('login_button').click()
