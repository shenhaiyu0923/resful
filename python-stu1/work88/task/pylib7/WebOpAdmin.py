from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cfg5 import *
import time

class WebOpAdmin():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setupWebTest(self,driverType='chrome'):
        self.driver=None
        if driverType=='chrome':
            self.driver=webdriver.Chrome()
        else:
            raise Exception('未知的浏览器 %s' % driverType)
        self.driver.implicitly_wait(10)

    def tearDownWebTest(self):
        self.driver.quit()

    def 登录(self):
        self.driver.get(mgrloginurl)
        self.driver.find_element_by_id('username').send_keys(user1['name'])
        self.driver.find_element_by_id('password').send_keys(user1['pwd'])
        self.driver.find_element_by_tag_name('button').click()
        # self.cur_wd.get(mgrloginurl)
        # self.cur_wd.find_element_by_id('username').send_keys(adminuser['name'])
        # self.cur_wd.find_element_by_id('password').send_keys(adminuser['pw'])
        # self.cur_wd.find_element_by_tag_name('button').click()
    def 退出(self):
        self.driver.find_element_by_css_selector('button[ng-click="logout()"]').click()
        time.sleep(2)
    def deleteAllc(self):
        self.driver.find_element_by_css_selector('a[ui-sref="course"]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            cur=self.driver.find_elements_by_css_selector('*[ng-click="delOne(one)"]')
            if cur==[]:
                break
            cur[0].click()
            self.driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    def deleteAllt(self):
        self.driver.find_element_by_css_selector('a[ui-sref="teacher"]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            cur=self.driver.find_elements_by_css_selector('*[ng-click="delOne(one)"]')
            if cur==[]:
                break
            cur[0].click()
            self.driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    def 增加课程(self,name,desc,idx):
        self.driver.find_elements_by_css_selector('a[ui-sref="course"]')
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        ele=self.driver.find_element_by_css_selector('input[ng-model="addData.name"]')
        ele.clear()
        ele.send_keys(name)
        ele=self.driver.find_element_by_tag_name("textarea")
        ele.clear()
        ele.send_keys(desc)
        ele=self.driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)
        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
        self.driver.find_element_by_css_selector('button[ng-click="$parent.showAddOne=false"]').click()
        time.sleep(1)

    def 增加老师(self,realname,username,desc,idx,course):

        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()

        ele = self.driver.find_element_by_css_selector(
            "input[ng-model='addEditData.realname']")
        ele.clear()
        ele.send_keys(realname)

        ele = self.driver.find_element_by_css_selector(
            "input[ng-model='addEditData.username']")
        ele.clear()
        ele.send_keys(username)

        ele = self.driver.find_element_by_css_selector(
            "textarea[ng-model='addEditData.desc']")
        ele.clear()
        ele.send_keys(desc)

        ele = self.driver.find_element_by_css_selector(
            "input[ng-model='addEditData.display_idx']")
        ele.clear()
        ele.send_keys(idx)

        select = Select(self.driver.find_element_by_css_selector(
            'select[ng-model*=courseSelected]'))
        select.select_by_visible_text(course)

        self.driver.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()

        time.sleep(1)



    def 检查老师(self):
        self.driver.find_element_by_css_selector('ul.nav a[href*=teacher]').click()
        eles=self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        print([ele.text for ele in eles])
        return [ele.text for ele in eles]

    def 检查课程(self):
        self.driver.find_element_by_css_selector('a[ui-sref="course"]').click()
        eles=self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        return [ele.text for ele in eles]


