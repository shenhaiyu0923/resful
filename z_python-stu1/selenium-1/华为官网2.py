import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('https://www.vmall.com/')
#进入华为官网
driver.find_element_by_css_selector('li:nth-child(2)>a').click()

def custom():
    eles=driver.find_elements_by_css_selector('.nav-cnt>li')
    actual_msg='|'.join([ele.text for ele in eles])#列表
    print([ele.text for ele in eles])
    tem='''智能手机
      笔记本
      平板
      智能穿戴
      智能家居
      更多产品
      软件应用
      服务与支持'''
    expect_msg='|'.join([s.strip() for s in tem.split('\n')])

    if actual_msg==expect_msg:
        print('pass')
    else:
        print(actual_msg)
        print(expect_msg)
        print('fail')

def shop():
    move=driver.find_element_by_id('zxnav_1')
    ActionChains(driver).move_to_element(move).perform()
    eles=driver.find_elements_by_css_selector('#zxnav_1 .subcate-item')
    expect_msg='|'.join([s.strip() for s in '平板电脑 笔记本电脑 笔记本配件'.split(' ')])
    print(expect_msg)
    actual_msg='|'.join([ele.text for ele in eles])
    print(actual_msg)
    if expect_msg==actual_msg:
        print('pass')
    else:
        print(actual_msg)
        print('fail')

for handel in driver.window_handles:
    driver.switch_to.window(handel)
    if '华为消费者' in driver.title:
        custom()
    elif '华为商城' in driver.title:
        shop()
    else:
        print('失败')
driver.quit()

