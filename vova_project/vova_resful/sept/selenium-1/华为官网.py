import time

from selenium import  webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

#华为商城
driver.get('https://www.vmall.com/')

#进入华为官网
driver.find_element_by_css_selector('[href="http://consumer.huawei.com/cn/"]').click()

def check_vconsumer():
    eles=driver.find_elements_by_css_selector('.nav-cnt>li')
    actual_msg='|'.join([ele.text for ele in eles])
    print([ele.text for ele in eles])
    tmp='''  智能手机
      笔记本
      平板
      智能穿戴
      智能家居
      更多产品
      软件应用
      服务与支持'''

    expect_msg='|'.join([s.strip() for s in tmp.split('\n')])
    print(expect_msg)

    if actual_msg==actual_msg:
        print('pass')
    else:
        print(actual_msg)
        print('fail')

#setTimeout(function(){debugger},3000)
def check_vmall():
    #移动鼠标到笔记本平板菜单
    move=driver.find_element_by_id('zxnav_1')
    ActionChains(driver).move_to_element(move).perform()
    time.sleep(2)
    eles=driver.find_elements_by_css_selector('#zxnav_1 .subcate-item')
    expect_msg= '|'.join([s.strip() for s in '平板电脑 笔记本电脑 笔记本配件'.split(' ')])

    print(expect_msg)
    actual_msg='|'.join([ele.text for ele in eles])
    if expect_msg==actual_msg:
        print('pass')
    else:
        print(actual_msg)
        print('fail')

default_hadel=driver.current_window_handle

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '华为商城' in driver.title:
        check_vmall()
    if  '华为消费者' in driver.title:
        driver.maximize_window()  # 最大化
        time.sleep(2)
        check_vconsumer()

driver.switch_to.window(default_hadel)
time.sleep(2)
driver.quit()
