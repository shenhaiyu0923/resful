import uiautomator2 as u2
import time
d = u2.connect("feeec6d8")
d.set_fastinput_ime(True)
s = d.session("com.netease.cloudmusic")
time.sleep(5)
d.xpath('//*[@resource-id="com.netease.cloudmusic:id/aus"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()

d.xpath('//*[@resource-id="com.netease.cloudmusic:id/ami"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
