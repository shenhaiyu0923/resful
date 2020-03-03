# 配置要获取多少条文章的标题
NUM = 100

from appium import webdriver
import time,traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'xxx',
    'automationName': 'UIAutomator2',
    'appPackage': 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
}


#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(4)



try:

    allTitles = []
    driver.find_element_by_id("home_feature_recycler_view")
    time.sleep(1)

    screenSize = driver.get_window_size()
    screenW = screenSize['width']
    screenH = screenSize['height']
    print(screenW,screenH)

    x = screenW / 2
    y1 = int(screenH * 0.8)
    y2 = int(screenH * 0.4)


    while True:
        pageTitleEles = driver.find_elements_by_id("tv_title")
        pageTitles = [one.text for one in pageTitleEles]
        for title in pageTitles:
            if title not in allTitles:
                allTitles.append(title)
                if len(allTitles) >= NUM:
                    break

        if len(allTitles) >= NUM:
            break

        driver.swipe(x, y1, x, y2, 1000)

    print('\n'.join(allTitles))

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()


