from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.51job.com')

#点击高级搜索
driver.find_element_by_css_selector("div.ush >a").click()
#输入关键字
driver.find_element_by_id("kwdselectid").send_keys("python")
#点击城市
driver.find_element_by_css_selector("#work_position_click").click()
#去掉已选择城市

cityEles=driver.find_elements_by_css_selector("#work_position_click_multiple_selected em")

for one in cityEles:
    one.click()
#选择杭州
driver.find_element_by_id("work_position_click_center_right_list_category_000000_080200").click()

#点击确定
driver.find_element_by_id("work_position_click_bottom_save").click()
#点击别处,等待回填
driver.find_element_by_css_selector("div.tit").click()

driver.find_element_by_id("funtype_click").click()

driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_0106").click()
#点击确定
driver.find_element_by_id("funtype_click_bottom_save").click()
# 公司性质选 外资 欧美
driver.find_element_by_id("cottype_list").click()
driver.find_element_by_css_selector("#cottype_list span.li[data-value='01']").click()
#工作年限
driver.find_element_by_id("workyear_list").click()
driver.find_element_by_css_selector("#workyear_list span.li[data-value='02']").click()

#点击搜索
driver.find_element_by_css_selector('.p_but').click()

jobs = driver.find_elements_by_css_selector('#resultList  div.el')

for job in jobs[1:]:
    msg=job.text.split('\n')
    print(' | '.join(msg))
time.sleep(3)
driver.quit()
