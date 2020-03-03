from PIL import Image
import pytesseract
from selenium import webdriver
import time
#根据驱动的实际路径填写
executable_path = r"d:\chromedriver\chromedriver.exe"
#初始化，运行chrome driver
driver = webdriver.Chrome(executable_path)
driver.maximize_window()
driver.get('http://vip.ytesting.com')
time.sleep(1)
driver.save_screenshot('page.png')#截图
verifyimg = driver.find_element_by_id('randCodeImage')
time.sleep(1)
left = verifyimg.location['x']
top = verifyimg.location['y']
right = verifyimg.location['x'] + verifyimg.size['width']
bottom = verifyimg.location['y'] + verifyimg.size['height']
img = Image.open('./page.png')
img = img.crop((left,top,right,bottom))
img.save('./code.png')

image = Image.open('./code.png')
code = pytesseract.image_to_string(image).replace('|','').replace(' ','').replace(']','')[1:]
print('该页面的验证码是:{}'.format(code))

driver.find_element_by_id('userName').send_keys('K201905165203')
driver.find_element_by_id('password').send_keys('1802161998')
driver.find_element_by_id('randCode').send_keys(code)
driver.find_element_by_id('but_login').click()
time.sleep(2)


ele = driver.find_element_by_class_name('form-control')
print(ele.text)
if ele.text == '欢迎登录松勤VIP管理系统':
    print('pass')
else:
    print('fail')
# driver.close()

