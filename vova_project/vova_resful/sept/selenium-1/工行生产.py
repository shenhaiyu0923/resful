from selenium import webdriver
import time
from PIL import Image
import pytesseract
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://efrs.icbc.com.cn/icbc/efrsnew/#/?val=home")
driver.maximize_window()
#setTimeout(function(){debugger},3000)
def yzm():
    driver.save_screenshot('page.png')  # 截图
    verifyimg = driver.find_element_by_css_selector("img.validation_code")
    print(verifyimg)

    left = verifyimg.location['x']
    top = verifyimg.location['y']
    right = verifyimg.location['x'] + verifyimg.size['width']
    bottom = verifyimg.location['y'] + verifyimg.size['height']
    img = Image.open('./page.png')
    img = img.crop((left, top, right, bottom))
    img.save('./code.png')
    image = Image.open('./code.png')
    code = pytesseract.image_to_string(image)
    print('该页面的验证码是:{}'.format(code))
    driver.find_element_by_id("pubkey").send_keys(code)
    driver.find_element_by_css_selector('div.login_btn_box.clearfix').click()


#首次点击登录

driver.find_element_by_css_selector("i.user_name").click()
#输入用户名密码
driver.find_element_by_id("userid").send_keys('1234567')
driver.find_element_by_id("password").send_keys('1234567')

yzm()
while True:
    time.sleep(2)
    loginN = driver.find_element_by_css_selector('span.bank_user i:nth-child(2)')
    print(loginN.text)
    if loginN.text=='测试名称':
        # 登录后进行下一步操作
        driver.find_element_by_css_selector('div.sec-content>input').send_keys('工商银行')
        driver.find_element_by_css_selector('div.sec-content button').click()  # 点击查询
        break
    # 验证码错误的话,需要点击错误提示弹窗
    else:
        driver.find_element_by_css_selector('div.un-message-box__btns span').click()
        print()
        yzm()
time.sleep(2)
driver.find_element_by_css_selector('div.company_msg[index="2"]').click() #中国工商银行上海市分行
#driver.find_element_by_id('nav-main-ALTER').click()
time.sleep(2)

default_hadel=driver.current_window_handle

driver.switch_to.window(default_hadel)
driver.find_element_by_css_selector('span.bank_user i:nth-child(2)').click()#点击用户名1234
time.sleep(2)
move = driver.find_element_by_css_selector('span.bank_user li:nth-child(1)')#移动到管理端按钮
ActionChains(driver).move_to_element(move).perform()
driver.find_element_by_css_selector('span.bank_user li:nth-child(1)').click()#点击管理端按钮
time.sleep(4)
driver.find_element_by_css_selector('tbody > tr:nth-child(1)').click()#点击1234567
driver.find_element_by_css_selector('button.create_user.operation_btn.bg2').click()#点击修改
driver.find_element_by_css_selector('div.add_user_main_box > div:nth-child(2) > div > input[type=text]').clear()
driver.find_element_by_css_selector('div.add_user_main_box > div:nth-child(2) > div > input[type=text]').send_keys('测试名称')

driver.find_element_by_css_selector('div:nth-child(6) input[type=text]').send_keys('测试描述信息')
driver.find_element_by_css_selector('div.add_user_btn_box > button').click()
driver.find_element_by_css_selector('div.un-message-box__btns > button > span').click()

time.sleep(5)

driver.quit()













