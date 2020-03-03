from  selenium import webdriver   #导入库
import time,traceback  #本地库
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.get_cookies())
time.sleep(1)
element_keyword=driver.find_element_by_id('kw')
time.sleep(1)
element_keyword.send_keys('中国工商银行')
time.sleep(1)
driver.find_element_by_id('su').click()
time.sleep(1)
driver.quit()
time.sleep(1)