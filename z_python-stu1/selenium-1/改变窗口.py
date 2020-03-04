from selenium import webdriver
import time
import win32api
import win32con

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.set_window_size(200,200)
size=driver.get_window_size()
print(size)
time.sleep(1)
driver.maximize_window()#最大化
time.sleep(1)
import winsound
winsound.Beep(1000,2000)#提示声音1000是频率,2000是时间
import os
#os.system('xxx.mp3')#用音乐提示


driver.find_element_by_id("kw").send_keys("松勤")
driver.find_element_by_id("su").click()
driver.execute_script('scrollBy(0,2000)')
time.sleep(2)
driver.find_element_by_css_selector('th:nth-child(1)>a').click()
for i in range(10):
    win32api.keybd_event(win32con.VK_DOWN,0)#VK_DOWN向下  #VK_DOWN向右  键盘点击移动  ,运用之前要获取到页面一个静态元素,保证鼠标在页面上
time.sleep(20)#等待两秒钟

driver.quit()
