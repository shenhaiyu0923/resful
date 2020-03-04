#coding:utf-8
from selenium import webdriver
import time

url = 'http://www.baidu.com'

# 创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数
# 设置浏览器为无头模式
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# 更换ip代理，必须冲新启动浏览器
# opt.add_argument('--proxy-server=http://113.254.44.242:8382')
# 更换user-agent
opt.add_argument('--user-agent=Mozilla/5.0 python37')



# 创建浏览器对象的时候添加配置对象
driver = webdriver.Chrome(chrome_options=opt)

driver.get(url)
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
time.sleep(4)
driver.save_screenshot('baidu_到期一游.png')