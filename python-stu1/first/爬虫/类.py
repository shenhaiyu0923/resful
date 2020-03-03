""" Created on 2019-03-28 @author: tangchunli Project：类和实例 """

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def print_grade(self):
        print(self.name, self.score, self.get_grade())
bob = Student('Bob', 81)
bob.print_grade()
