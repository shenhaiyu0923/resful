# coding=utf-8
from selenium import webdriver
import  time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://music.163.com/')

driver.switch_to.frame('g_iframe')

banner2=driver.find_element_by_css_selector('img[class="d-flag"]')

banner2.screenshot('网易云.png')
driver.quit()


# 7、浏览器进入网页云音乐  https://music.163.com/
# 在首页的发现音乐菜单，点击进入排行榜>云音乐新歌版
# 查看排名前三的歌曲下的评论，在精彩评论部分找到点赞数量最高的评论，获取评论作者，内容，时间和当前点赞数量
