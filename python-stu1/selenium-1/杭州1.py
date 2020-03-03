from selenium import webdriver
import time
driver=webdriver.Chrome()

driver.get('http://www.51job.com')

driver.find_element_by_id("kwdselectid").send_keys("python")

driver.find_element_by_id("work_position_input").click()

cityEles=driver.find_element_by_id("work_position_click_multiple")
cityEles=driver.find_elements_by_css_selector("#work_position_click_multiple_selected em")

for one in cityEles:
    one.click()
#选择杭州
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()
#点击确定
time.sleep(1)
driver.find_element_by_id("work_position_click_bottom_save").click()
#点击搜索
driver.find_element_by_css_selector('.ush  button').click()

jobs = driver.find_elements_by_css_selector('#resultList  div.el')

for job in jobs[1:]:
    msg=job.text.split('\n')
    print(' | '.join(msg))
driver.quit()
