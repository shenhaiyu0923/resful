from appium import webdriver
import time


desired_caps = {
    'platformName': 'Android',
    '': '9',
    'deviceName': 'xxx',
#     'app' : r'e:\apk\sqauto.apk',
    'appPackage': 'com.sqauto',
    'appActivity': 'com.sqauto.MainActivity',
    'noReset': True,
    'newCommandTimeout': 6000,
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

size=driver.get_window_size()
x=size['width']*0.5
y1=size['height']*0.6
y2=size['height']*0.3
res=[]
driver.implicitly_wait(0.5)
while True:
    driver.swipe(x,y1,x,y2,800)#防止惯性
    #kb=driver.find_element_by_accessibility_id('best reputation')#content-desc
    kb = driver.find_elements_by_xpath('//*[@text="口碑最佳"]')
    #xpath='//android.widget.TextView[@content-desc="best reputation"]'
    if kb:
        xpath='//*[@content-desc="best reputation"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]'
        kb_app=driver.find_elements_by_xpath(xpath)
        app_names = [app.text for app in kb_app]
        res.extend(app_names)
    #za=driver.find_elements_by_xpath('//*[@text="用户最爱"]')
    za=driver.find_elements_by_accessibility_id('user favorite')
    if za:
        za_apps=driver.find_elements_by_xpath('//*[@text="用户最爱"]/following-sibling::android.widget.ImageView/following-sibling::android.widget.TextView[1]')
        za_app_names=[app.text for app in za_apps]
        break

for z in za_app_names:
    if z in res:
        res.remove(z)


driver.implicitly_wait(1)
print('口碑最佳的应用有:')
print(set(res))
[print(ele) for ele in set(res)]



