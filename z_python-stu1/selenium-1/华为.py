from selenium import  webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get('https://www.vmall.com/')


driver.find_element_by_css_selector(
    'a[href="http://consumer.huawei.com/cn/"]'
).click()


driver.find_element_by_css_selector(
    '.s-sub li:nth-last-child(1)'
).click()

driver.find_element_by_css_selector(
    'a[href="http://appstore.huawei.com/"]'
).click()


def checkHuaWei():
    expected = '智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'

    # 注意窗口的宽度决定显示多少个菜单，可能需要拉宽窗口
    # 先不写下面的代码，发现错误再添加
    size = driver.get_window_size()
    driver.set_window_size(1500, size['height'])

    eles = driver.find_elements_by_css_selector(".left-box .nav-cnt > li")
    eleTexts = [ele.text for ele in eles]


    actual = '|'.join(eleTexts)
    if actual == expected:
        print('huawei page pass')
    else:
        print('huawei page fail!!!!')


def checkVmail():
    expected = '''平板电脑|笔记本电脑|笔记本配件'''
    from selenium.webdriver.common.action_chains import ActionChains
    ac = ActionChains(driver)

    ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

    # 用 setTimeout(function(){debugger;},3000) 来 查看元素
    # 分析 得知  zxnav_1 ，2,3,4  分别就是对应 菜单的，里面有隐藏菜单
    eles = driver.find_elements_by_css_selector('#zxnav_1 .subcate-item a span')
    eleTexts = [ele.text for ele in eles]
    actual = '|'.join(eleTexts)
    if actual == expected:
        print('main page pass')
    else:
        print('main page fail!!!!')


for handle in driver.window_handles:
    driver.switch_to.window(handle)

    if '消费者业务官网' in driver.title:
        checkHuaWei()
    else:
        checkVmail()

driver.quit()
