import uiautomator2 as u2
import time
d = u2.connect('127.0.0.1')
#d.session('com.vova.android')


d.click_post_delay = 1  #设置每次单击UI并单击后的延迟1s
d.wait_timeout = 30.0#＃设置默认元素等待超时（秒）
d.set_fastinput_ime(True)
d.app_clear('com.vova.android')
d.app_start('com.vova.android')

# d(resourceId="com.vova.android:id/rl_famale_layout").click()#选择性别
# d(resourceId="com.vova.android:id/txt_under_18").click()#选择年龄
d(resourceId="com.vova.android:id/account_animation_view").click()#点击me
d(resourceId="com.vova.android:id/tv_get_it").click()#点击get it
d(resourceId="com.vova.android:id/tv_get_it").click()#点击get it

d(resourceId="com.vova.android:id/tv_sign_in").click()
d(resourceId="com.vova.android:id/et_account").send_keys('p1210@tetx.com')#点击填写邮箱
d(resourceId="com.vova.android:id/et_psw").send_keys('111111')#点击填写密码
d(resourceId="com.vova.android:id/btn_submit").click()#点击登陆
login_name = d(resourceId="com.vova.android:id/tv_user_name").info["text"]
print(login_name)



