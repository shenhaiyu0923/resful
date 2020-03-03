from appium import webdriver
from p7.cfg import *
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'platformVersion': '7',
    'deviceName': 'xxx',
    'appPackage': 'com.yjyxapp',
    'appActivity': 'com.yjyxapp.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
}


class MobileAdmin:

    def open_mobile(self):
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps

        )
        self.driver.implicitly_wait(10)

    def vcode_login(self,vcode):


        # 输入vcode
        code = 'new UiSelector().text("请输入vcode")'
        ele = self.driver.find_element_by_android_uiautomator(code)
        ele.send_keys(vcode)


        # 点击登录
        code = 'new UiSelector().text("登录")'
        ele = self.driver.find_element_by_android_uiautomator(code)
        ele.click()


        # 判断是否登录成功
        eles = self.driver.find_elements_by_id('android:id/alertTitle')

        # 找到Alert对话框，登录失败
        if eles:
            errInfo = self.driver.find_element_by_id('android:id/message').text
            print(errInfo)

            return {'ret':False, 'info':errInfo}

        # 登录成功
        else:
            return {'ret':True}


    def reset_app(self):
        self.driver.reset()


    def close_mobile(self):
        self.driver.quit()

ins_MobileAdmin = MobileAdmin()
# ins_MobileAdmin.vcode_login('3w32423423')