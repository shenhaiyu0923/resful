# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender == ('female'or'male'):
            self.__gender = gender
        else:
            raise ValueError('bad gender')

bart = Student('Bart','male')
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    if bart.get_gender()!='female':
        print(bart.get_gender())
        print('测试失败！')
    else:
        print(bart.get_gender())
        print('测试成功！')