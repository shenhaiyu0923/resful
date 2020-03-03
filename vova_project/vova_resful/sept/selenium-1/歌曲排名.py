from selenium import webdriver


driver=webdriver.Firefox()

driver.get('http://music.baidu.com/top/new')

div=driver.find_element_by_id("songListWrapper")
ul=div.find_element_by_tag_name("ul")
lilist=ul.find_elements_by_tag_name('li')
for li in lilist:
    upTags=li.find_elements_by_class_name("up")
    if upTags:
        title=li.find_element_by_class_name("song-title")
        titleStr=title.find_element_by_tag_name("a").text
        authorsStr = li.find_element_by_class_name("author_list").text
        print('{:10s}:{}'.format(titleStr, authorsStr))
driver.quit()















