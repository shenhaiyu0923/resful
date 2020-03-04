import uiautomator2 as u2
import time
from pprint import pprint
from p9.cfg import *
#127.0.0.1:62001
class Mobileyiyx101101:
    def open_mobile(self):
        self.d = u2.connect("feeec6d8")  # adb devices
        #self.d = u2.connect("127.0.0.1")
        self.d.set_fastinput_ime(True)
        s = self.d.session("com.yjyxapp")
    def vcode_login(self,vcode):
        self.d(text="请输入vcode").click()
        self.d.send_keys(vcode, clear=True)
        self.d(text="登录").click()
        time.sleep(1)
        self.d.screenshot('abc.png')

        if self.d(resourceId="android:id/message"):
            a=self.d(resourceId="android:id/message").info   #infi是获取元素信息
            pprint(a)
            print(a["text"])
        self.d(resourceId="android:id/button1").click()

ins_MobileAdmin = Mobileyiyx101101()
ins_MobileAdmin.open_mobile()
ins_MobileAdmin.vcode_login("123")


