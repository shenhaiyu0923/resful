# coding=utf8

from appium import webdriver
import time, traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'xxx',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',#门牌号
#    'unicodeKeyboard': True,
 #   'resetKeyboard': True,
    'noReset': True,#避免清除信息
    'newCommandTimeout': 6000,#设置超时
}
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
try:


    # 根据id找到元素，并点击，id和 html 元素的id不同
    driver.find_element_by_id("tab_bar_plus").click()
    time.sleep(1)
    p_ele=driver.find_elements_by_id("tv_tab_title")
    p_ele[1].click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("edt_phone")
    ele.send_keys('13656410395')
    ele = driver.find_element_by_id("edt_password")
    ele.send_keys('guiji0923')
    time.sleep(1)
    # 点击登录
    driver.find_element_by_id('btn_login').click()
    pass

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()

