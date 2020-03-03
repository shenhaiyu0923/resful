# from selenium import webdriver
#
# # 指定driver的绝对路径,如果driver已经添加到了环境变量中则不需指定
# driver = webdriver.PhantomJS(executable_path='./chromedriver')
# driver = webdriver.Chrome()
#
# # 向一个url发起请求
# driver.get("http://www.itcast.cn/")
#
# # 把网页保存为图片，69版本以上的谷歌浏览器将无法使用截图功能
# # driver.save_screenshot("itcast.png")
#
# print(driver.title) # 打印页面的标题
#
# # 退出模拟浏览器
# driver.quit() # 一定要退出！不退出会有残留进程！


from selenium import webdriver

# 指定driver的绝对路径
driver = webdriver.PhantomJS()
# driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

# 向一个url发起请求
driver.get("http://www.itcast.cn/")

# 把网页保存为图片
driver.save_screenshot("itcast.png")

# 退出模拟浏览器
driver.quit() # 一定要退出！不退出会有残留进程！


# response = requests.get(url)