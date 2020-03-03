from cfg import *

class login():
    def open_mobile(self,):
        d.set_fastinput_ime(True)
        d.app_clear(vova_android)
        d.app_start(vova_android)
        #d.session(vova_android)


#初始化登陆操作
    def email_login(self,emial,pwd):
        d.set_fastinput_ime(True)
        d.click_post_delay = 1  #设置每次单击UI并单击后的延迟0.5s
        d.wait_timeout = 30.0#＃设置默认元素等待超时（秒）
        d(resourceId="com.vova.android:id/rl_famale_layout").click()#选择性别
        d(resourceId="com.vova.android:id/txt_under_18").click()#选择年龄
        d(resourceId="com.vova.android:id/account_animation_view").click()#点击me
        d(resourceId="com.vova.android:id/tv_get_it").click()#点击get it
        d(resourceId="com.vova.android:id/tv_get_it").click()#点击get it
        d(resourceId="com.vova.android:id/tv_sign_in").click()
        d(resourceId="com.vova.android:id/et_account").send_keys(emial)#点击填写邮箱
        d(resourceId="com.vova.android:id/et_psw").send_keys(pwd)#点击填写密码
        d(resourceId="com.vova.android:id/btn_submit").click()#点击登陆
        time.sleep(5)
        login_name = d(resourceId="com.vova.android:id/tv_user_name").info["text"]
        return login_name

login = login()

