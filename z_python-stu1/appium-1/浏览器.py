# coding=utf8

from appium import webdriver
import time, traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'xxx',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'com.vivo.browser',
    'appActivity': '.BrowserActivity',#门牌号
#    'unicodeKeyboard': True,
 #   'resetKeyboard': True,
    'noReset': True,#避免清除信息
    'newCommandTimeout': 6000,#设置超时
}
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
print('===========================================')
driver.open_notifications()#打开通知栏
time.sleep(3)
driver.press_keycode(4)#模拟返回键
driver.press_keycode(5)#模拟拨电话
time.sleep(10)
driver.quit()

