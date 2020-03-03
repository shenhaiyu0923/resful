from appium import webdriver
import time,traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'xxx',
    'appPackage': 'com.ibox.calculators',
    'appActivity': '.SplashActivity',
#   'unicodeKeyboard': True,
#   'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

def cacul(id):
    driver.find_element_by_id(id).click()

cacul('digit3')
'''
cacul('plus')
cacul('digit9')
cacul('equal')
cacul('mul')
cacul('digit5')
cacul('equal')
'''

time.sleep(1)
driver.tap([(900,1500)])#+

driver.tap([(650,1000)],3000)#9.,--------长按三秒钟

driver.tap([(900,1800)])#=

driver.tap([(900,1000)])#x

driver.tap([(400,1250)])#=

driver.tap([(900,1800)])#=
time.sleep(1)


p_ele=driver.find_element_by_id('cv')
retStr=p_ele.find_elements_by_class_name('android.widget.TextView')


print(retStr[1].text)

if retStr[1].text=='60':
    print('pass')
else:
    print(retStr[1].text)

driver.quit()


