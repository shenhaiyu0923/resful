from selenium import webdriver
import time
driver=webdriver.Firefox()
#driver = webdriver.Chrome("d://chromedriver/chromedriver.exe")
#打开浏览器
driver.get("http://www.baidu.com")

#通过元素寻找
ele=driver.find_element_by_id("kw")
time.sleep(2)#等待两秒钟
ele.send_keys("松勤")

ele2=driver.find_element_by_id("su")
ele2.click()

#关闭浏览器,彻底关闭chromedriver.exe,colse是关闭了浏览器窗口
#driver.quit()
time.sleep(2)#等待两秒钟

