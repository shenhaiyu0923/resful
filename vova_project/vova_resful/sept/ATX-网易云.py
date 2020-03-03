import uiautomator2 as u2
import time
#d = u2.connect("feeec6d8")  #vivo手机
#d= u2.connect("192.168.4.85")  ##vivo手机
d = u2.connect('127.0.0.1:62001')
d.set_fastinput_ime(True)
d.wait_timeout
d.screen_on()#打开屏幕
d.drag(0.46, 0.856,0.465, 0.131,0.05)
# d.xpath('//*[@text="9"]').click()
# d.xpath('//*[@text="2"]').click()
# d.xpath('//*[@text="3"]').click()
# d.xpath('//*[@text="9"]').click()
# d.xpath('//*[@text="2"]').click()
# d.xpath('//*[@text="3"]').click()
d.click(0.586, 0.816)
d.click(0.383, 0.679)
d.click(0.574, 0.678)
d.click(0.586, 0.816)
d.click(0.383, 0.679)
d.click(0.574, 0.678)
s = d.session("com.netease.cloudmusic")
d.xpath('//*[@resource-id="com.netease.cloudmusic:id/ata"]').click()
for i in range(3):
    d.drag(0.46, 0.856,0.465, 0.131,0.05)#滑动页面，0.05是滑动时间
    if d.xpath('//android.widget.FrameLayout[1]')==True:
        break

d.screenshot("home.jpg")
d.xpath('//android.widget.FrameLayout[1]').click()
#d.screen_off()#关闭屏幕


#d.screen_off()#关闭屏幕