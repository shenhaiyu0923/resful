from selenium import webdriver
import time
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup

driver=webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://efrs.icbc.com.cn/icbc/efrsnew/")
#点击登录
time.sleep(5)
driver.find_element_by_css_selector("i.user_name").click()
#用户名
driver.find_element_by_id("userid").send_keys('1234567')

driver.find_element_by_id("password").send_keys('1234567')

ele=driver.find_element_by_css_selector("img.validation_code")
a=ele.get_attribute('src')
print(a)


driver.save_screenshot('page.png')#截图
verifyimg=driver.find_element_by_css_selector("img.validation_code")
print(verifyimg)

time.sleep(3)
left = verifyimg.location['x']
top = verifyimg.location['y']
right = verifyimg.location['x'] + verifyimg.size['width']
bottom = verifyimg.location['y'] + verifyimg.size['height']
img = Image.open('./page.png')
img = img.crop((left,top,right,bottom))
img.save('./code.png')
image = Image.open('./code.png')
code = pytesseract.image_to_string(image)
print('该页面的验证码是:{}'.format(code))
driver.find_element_by_id("pubkey").send_keys(code)

