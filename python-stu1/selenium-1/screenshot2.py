# coding=utf-8
from selenium import webdriver
import  time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://music.163.com/')

driver.switch_to.frame('g_iframe')

banner=driver.find_element_by_id('index-banner')
#banner2=driver.find_element_by_css_selector('img[class="d-flag"]')

banner.screenshot('d:\\banner.png')

png=banner.screenshot_as_png

with open('d:\\banner2.png','ab') as f:
    f.write(png)

input('press any key to quit...')
driver.quit()   # 浏览器退出