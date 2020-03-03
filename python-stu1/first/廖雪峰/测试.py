from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Call():
    dr = webdriver.Firefox() #把浏览器作为全局变量
    def login(self): #调用全局变量进行登录
        Call.dr.get("http://localhost:8080/WoniuBoss2.0/")
        Call.dr.maximize_window()#窗口最大化
        Call.dr.find_element_by_name("userName").send_keys("WNCD001")
        Call.dr.find_element_by_name("userPass").send_keys("woniu123")
        Call.dr.find_element_by_css_selector("button.btn.btn-primary.btn-block.btn-save").click()
        # Call.dr.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        # assert Call.dr.find_element_by_xpath("/html/body/div[2]/div[1]/img").is_displayed() == True
                                             #is_displayed()显示 ，is_selected()选中,is_enabled()启动

    def decode(self): #解密
        Call.dr.find_element_by_id("btn-decrypt").click()
        time.sleep(1)
        Call.dr.find_element_by_name("secondPass").send_keys("woniu123")
        Call.dr.find_element_by_css_selector("button.btn.btn-info").click()

    def click_course(self): #点击新增排课

        Call.dr.find_element_by_xpath("//div[@id='nav2']/a[5]").click()
        Call.dr.find_element_by_xpath("/html/body/div[7]/div[2]/div/ul/li[9]/a").click()
        Call.dr.find_element_by_xpath("//div[@id='course']/div/button").click()

    def add_time(self):#时间
        Call.dr.find_element_by_css_selector("input[name='cur.start_time']").send_keys(Keys.CONTROL,"a")
        Call.dr.find_element_by_xpath("//input[@name='cur.start_time']").send_keys("2019-1-17")
        Call.dr.find_element_by_css_selector("input[name='cur.end_time']").send_keys(Keys.CONTROL,'a')
        Call.dr.find_element_by_css_selector("input[name='cur.end_time']").send_keys("2019-1-18")

    def add_curriculum(self,data): #新增排课课程
        for i in range(1,10):
            Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[2]/form/table/tbody/tr[%s]/td[3]/select"%i).send_keys("休息")
            time.sleep(0.5)
            # print(i)
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[2]/form/table/tbody/tr[6]/td[3]/select").send_keys("正常")
        time.sleep(1)
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[2]/form/table/tbody/tr[6]/td[4]/select").send_keys(data["教室"])
        time.sleep(1)
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[2]/form/table/tbody/tr[6]/td[5]/select").send_keys(data["班号"])
        time.sleep(1)
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[2]/form/table/tbody/tr[6]/td[6]/select").send_keys(data["方向"])
        time.sleep(1)
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[2]/form/table/tbody/tr[6]/td[7]/select").send_keys(data["课程安排"])
        time.sleep(1)
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[3]/button[2]").click()
        # Call.dr.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
        Call.dr.find_element_by_xpath("/html/body/div[16]/div/div/div[1]/button").click()


if __name__ == '__main__':
    a = Call()
    a.login()