#coding:utf-8
from selenium import webdriver
import time


url='https://lfyanjiao.58.com/hezu/?PGTID=0d100000-0320-44c6-c018-2374633dc940&ClickID=2'
a='/html//div[2]/ul/li/div[2]/h2/a'
# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get(url)
el_list = driver.find_elements_by_xpath(a)
print(el_list)
# print(len(el_list))
# print(el_list)

for el in el_list:
    print(el)
    print(el.get_attribute('href'))
    print(el.get_attribute('text'))
driver.quit()
# el.send_keys(data), 该元素必须能够接受数据 input/text
# el.click()    该元素必须能够接受点击操作



'''
            try:
                temp['host_url'] = node.find_element_by_xpath('./div/div/div/ytd-video-meta-block/div/div/div/yt-formatted-string/a').get_attribute('href')
            except Exception as e:
                print(e)
            try:
                temp['show_url'] = node.find_element_by_xpath('./div/ytd-thumbnail/a').get_attribute('href')
            except Exception as e:
                print(e)
            try:
                temp['title'] = node.find_element_by_xpath('./div/div/div[1]/div/h3/a').get_attribute('title')
            except Exception as e:
                print(e)
            try:
                temp['user'] = node.find_element_by_xpath('./div/div/div/ytd-video-meta-block/div/div/div/yt-formatted-string/a').text

'''