from selenium import webdriver
import  time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()#最大化

driver.implicitly_wait(10)
driver.get('https://music.163.com/')
for i in range(1,4):
    driver.find_element_by_css_selector('#g_nav2 > div > ul > li:nth-child(2) > a > em').click()
    driver.switch_to.frame('g_iframe')
    driver.find_element_by_css_selector('ul:nth-child(2) > li:nth-child(2) p.name>a').click()
    time.sleep(2)
    value='tbody tr:nth-child({})'.format(i)
    list1=driver.find_element_by_css_selector(value)
    list1.find_element_by_tag_name('b').click()
    com=driver.find_element_by_css_selector('#comment-box div[class="itm"]:nth-child(2)')
    name=com.find_element_by_css_selector('a[class="s-fc7"]').text
    comm=com.find_element_by_css_selector('div[class="cnt f-brk"]').text
    time1=com.find_element_by_css_selector('div[class="time s-fc4"]').text
    num=com.find_element_by_css_selector('a:nth-child(2)').text
    print('作者:{0}\n评论:{1}\n时间:{2}\n评论数:{3}'.format(name, comm,time1,num))
    print(i)
    driver.back()
driver.quit()
