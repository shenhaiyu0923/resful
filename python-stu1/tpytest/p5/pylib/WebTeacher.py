from selenium import webdriver
from p5.cfg import *

import time

class WebTeacher:

    def teacher_login(self,username,password):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        self.driver.get(web_login_url)


        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)

        self.driver.find_element_by_id('submit').click()

    def get_teacher_homepage_info(self):

        self.driver.find_element_by_css_selector('a[href="#/home"] > li').click()  #点击主页

        time.sleep(1)

        eles = self.driver.find_elements_by_css_selector(
            '#home_div .ng-binding'
        )
        return [ele.text for ele in eles]


    def get_teacher_class_students_info(self):#点击班级学生信息

        self.driver.find_element_by_css_selector(
            '.main-menu > ul > li:nth-of-type(4)'
        ).click()#先点击班级情况

        self.driver.find_element_by_css_selector(
            "a[href='#/student_group'] span"
        ).click()#再点击班级学生

        time.sleep(1)#等待加载

        panels = self.driver.find_elements_by_css_selector(
            '.panel-green'
        )#查询班级数量

        if not panels:
            return {}

        classStudentTab = {}

        for panel in panels:
            gradeclass = panel.find_element_by_class_name('panel-heading').\
                text.replace(' ','')

            panel.click()

            time.sleep(2)

            self.driver.implicitly_wait(1)
            nameEles = panel.find_elements_by_css_selector(
                'tr > td:nth-child(2)'
            )
            self.driver.implicitly_wait(10)

            names = [nameEle.text for nameEle in nameEles]

            classStudentTab[gradeclass] = names

        return classStudentTab


ins_WebTeacher = WebTeacher()