
# coding=utf8

from appium import webdriver
import time ,traceback

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
#desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print(driver.session_id)
driver.implicitly_wait(10)

try:
    # -----------------

    # 用下面的表达式，也可以用xpath

    code = u'new UiSelector().resourceId("io.manong.developerdaily:id/btn_item").instance(0).childSelector(new UiSelector().className("android.widget.TextView"))'
    ele1 = driver.find_element_by_android_uiautomator(code)

    text1 = ele1.text
    print(text1)

    ele1.click()

    time.sleep(2)

    ele2 = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    text2 = ele2.text
    print (text2)

    if text2 == text1:
        print ('pass')
    else:
        print ('fail')


    driver.press_keycode(4)

    #  检查是否回到刚才的页面
    ele2 = driver.find_elements_by_id('io.manong.developerdaily:id/tab_bar_plus')

    if ele2:
        print( 'we return back')

    # -----------------

except:
    print (traceback.format_exc())

driver.quit()