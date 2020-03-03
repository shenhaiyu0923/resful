from appium import webdriver
import time,traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'xxx',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',#门牌号
#    'unicodeKeyboard': True,
 #   'resetKeyboard': True,
    'noReset': False,#避免清除信息
    'newCommandTimeout': 6000,#设置超时
}


#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:

    #io.manong.developerdaily: id / iv_tab_icon

    # 根据id找到元素，并点击，id和 html 元素的id不同
    driver.find_element_by_id("tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("btn_email").click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("edt_email")
#    ele.send_keys('jcyrss@163.com')
    ele.send_keys('1802161998@qq.com')
    ele = driver.find_element_by_id("edt_password")
#    ele.send_keys('sdfsdf')
    ele.send_keys('guiji0923')

    #time.sleep(2)
    driver.implicitly_wait(2)
    # 点击登录
    driver.find_element_by_id('btn_login').click()

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()


