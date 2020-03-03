from selenium import webdriver

driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")
driver.get("http://www.baidu.com")
print(driver.get_cookies())

element_keyword = driver.find_element_by_id("kw").send_keys("松勤")
element_search_button = driver.find_element_by_id("su").click()
driver.quit()

