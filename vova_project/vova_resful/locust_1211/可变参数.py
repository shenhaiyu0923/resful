studentInfo = {
    '张飞' :  18,
    '赵云' :  17,
    '许褚' :  16,
    '典韦' :  18,
    '关羽' :  19,
}

def  printAge(*students) :
    for  student in students:
        print( f'学生：{student} , 年龄 {studentInfo[student]}')

printAge('张飞', '典韦', '关羽')