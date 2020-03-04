from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
driver.implicitly_wait(10)
#起点
begin=driver.find_element_by_id('fromStationText')
begin.click()
begin.clear()
begin.send_keys('南京南\n')
#终点
toEle = driver.find_element_by_id('toStationText')
toEle.click()
toEle.clear()
toEle.send_keys('杭州东\n')
#发车时段
timeSelect=Select(driver.find_element_by_id('cc_start_time'))
#通过可见文本选择
timeSelect.select_by_visible_text('00:00--24:00')
#发车日期-后天
datetime = driver.find_element_by_css_selector('#date_range li:nth-child(3)')
datetime.click()

#寻找二等座有座的车次
print('\n\n\n===============================\n\n\n')
xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
#xpath='//*[@id="queryLeftTable"]//td[4][@class]/preceding-sibling::td[last()]//a'

theTrains = driver.find_elements_by_xpath(xpath)
for one in theTrains:
    print (one.text)
driver.quit()