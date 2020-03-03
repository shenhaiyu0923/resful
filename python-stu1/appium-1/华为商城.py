# coding=utf8
from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '9'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
#desired_caps['app'] = r'd:\apk\HiSpace.apk'  #app 文件 名，指定了要安装的app 在电脑上的路径
desired_caps['appPackage'] = 'com.huawei.appmarket'  #app package名,指定了要运行的app
desired_caps['appActivity'] = '.MainActivity' #app默认Activity
# desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
# desired_caps['automationName'] = 'uiautomator2'
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)


'''
window_size=driver.get_window_size()
height=window_size['height']
width=window_size['width']
start_x=width*0.5
end_y=height*0.1
start_y=height*0.9

try:
    for i in range(3):
        driver.swipe(start_x,start_y,start_x,end_y,2000)
        time.sleep(2)
except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()
'''


window_size=driver.get_window_size()
height=window_size['height']
width=window_size['width']
start_x=width*0.5
end_y=height*0.1
start_y=height*0.9

banner=driver.find_element_by_id('com.huawei.appmarket:id/backPicture')
leftop=banner.location

ele_size=banner.size

center_x=leftop['x']+ele_size['width']*0.5
center_y=leftop['y']+ele_size['height']*0.5

print(center_x,center_y)

start_x=leftop['x']+ele_size['width']*0.2
end_x=leftop['x']+ele_size['width']*0.8


try:
    for i in range(10):
        driver.swipe(start_x,center_y,end_x,center_y,200)
        time.sleep(0.2)
except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()