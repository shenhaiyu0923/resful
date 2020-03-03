from selenium import webdriver
import  time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()#最大化