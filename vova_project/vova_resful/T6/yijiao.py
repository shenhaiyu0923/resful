
from T6.initialize_id import *
from pprint import pprint

class Mobileyiyx101101():
    def open_mobile(self,):
        d.set_fastinput_ime(True)
        d.session("com.yjyxapp")

    @badpng
    def vcode_login(self,vcode):
        d(text="请输入vcode").click()
        d.send_keys(vcode, clear=True)
        d(text="登录").click()
        #assert d(resourceId="android:id/message")

        a=d(resourceId="android:id/message").info   #infi是获取元素信息
        pprint(a)
        print(a["text"])
        d(resourceId="android:id/button11").click()

ins_MobileAdmin = Mobileyiyx101101()
ins_MobileAdmin.open_mobile()
ins_MobileAdmin.vcode_login("123")

