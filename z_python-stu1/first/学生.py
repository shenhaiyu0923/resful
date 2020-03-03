def aaa():
    a = input('请按格式输入学生信息:')
    studentInfo = a.split(';')
    for one in studentInfo:
        if ',' not in one:
            print("格式不正确,请重新输入")
            aaa()
        name, age = one.split(',')
        name = name.strip()
        age = age.strip()
        #  check is age digit
        if not age.isdigit():
            print("年龄必须是数字")
            print("请重新输入:")
            aaa()
        age = int(age)
        print('信息输入成功')#
        print('%-20s :  %02d' % (name, age))
        aaa()
        # print('{:20} :  {:02}'.format(name, age))
        # print(f'{name:20} :  {age:02}')
aaa()