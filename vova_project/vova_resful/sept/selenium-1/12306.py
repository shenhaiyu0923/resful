from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

fromEle = driver.find_element_by_id('fromStationText')
# 为什么这里要点击一下
fromEle.click()

fromEle.clear()
fromEle.send_keys(u'南京南\n')

toEle = driver.find_element_by_id('toStationText')

toEle.click()
toEle.clear()
toEle.send_keys(u'杭州东\n')

# 输入开始时间，
timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('06:00--12:00')


tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(2)')
# 点击这个，就会搜索车次了
tomorrow.click()

# 方法一：用xpath实现获取二等座有票的车次信息
print('\n\n\n===============================\n\n\n')
xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'

theTrains = driver.find_elements_by_xpath(xpath)
for one in theTrains:
    print (one.text)



# 方法二：用css实现获取二等座有票的车次信息
print('\n\n\n===============================\n\n\n')
theTrainLines = driver.find_elements_by_css_selector('#queryLeftTable > tr')
# 先不加这个，发现特别慢
driver.implicitly_wait(0)
for one in theTrainLines:
    secondlevelseat = one.find_elements_by_css_selector('td:nth-of-type(4)[class]')
    if secondlevelseat:
        print (one.find_element_by_css_selector('td:nth-of-type(1) a').text)
driver.implicitly_wait(10)


driver.quit()