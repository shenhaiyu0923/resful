from selenium import webdriver
from p7.cfg import *
import time




class WebTeacher:

    def teacher_login(self,username,password):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

        self.driver.get('http://ci.ytesting.com/teacher/login/login.html')


        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)

        self.driver.find_element_by_id('submit').click()

    def get_teacher_homepage_info(self):

        self.driver.find_element_by_css_selector(
            'a[href="#/home"] > li'
        ).click()

        time.sleep(1)

        eles = self.driver.find_elements_by_css_selector(
            '#home_div .ng-binding'
        )


        return [ele.text for ele in eles]



    def get_teacher_class_students_info(self):

        self.driver.find_element_by_css_selector(
            '.main-menu > ul > li:nth-of-type(4)'
        ).click()

        self.driver.find_element_by_css_selector(
            "a[href='#/student_group'] span"
        ).click()

        time.sleep(1)

        panels = self.driver.find_elements_by_css_selector(
            '.panel-green'
        )

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