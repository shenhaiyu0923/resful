# coding: utf-8
#
import uiautomator2 as u2

#d = u2.connect("feeec6d8")
d = u2.connect("192.168.4.85")

print(d.serial)
print(d.window_size())
#print(d.current_app())
print(d.info)
d.screen_off()
#
# 1、安装apk：python -m uiautomator2 install $ device_ip https://example.org/some.apk
# 2、清缓存：python -m uiautomator2
# 3、停止所有应用程序：python -m uiautomator2 app-stop-all $ device_ip
# 4、截图：python -m uiautomator2截图$ device_ip screenshot.jpg
# 5、检查守护线程：d.healthcheck（）
# 6、打开调试：d.debug = true
# 7、获取连接信息：d.info
# 8、shell命令：d.adb_shell（'pwd'）
# 9、分辨率：d.window_size（）
# 10、查看当前应用信息：d.current_app（）
# 11、查看序列号：d.serial