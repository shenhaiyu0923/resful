# 请实现一个程序，实现如下需求点：
#
#
# 1.
# 程序开始的时候提示用户输入学生年龄信息
# 格式如下：
#
# Jack
# Green, 21;
# Mike
# Mos, 9;
#
# 我们假设
# 用户输入
# 上面的信息，必定会遵守下面的规则：
# 学生信息之间用分号隔开（分号前后可能有不定数量的空格），
# 每个学生信息里的
# 姓名和
# 年龄之间用
# 逗号隔开（逗号前后可能有不定数量的空格）
#
# 2.
# 程序随后将输入的学生信息分行显示，格式如下
# Jack
# Green: 21;
# Mike
# Mos: 0
# 9;
# 学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
#
#
#
# 【参考答案】在下面

inputStr = input('Please input student age info:')
studentInfo = inputStr.split(';')
for one in studentInfo:
    # check if it is valid input 
    if ',' not in one:
        continue

    name, age = one.split(',')
    name = name.strip()
    age = age.strip()

    #  check is age digit
    if not age.isdigit():
        continue

    age = int(age)

    print('%-20s :  %02d' % (name, age))
    # print('{:20} :  {:02}'.format(name, age))
    # print(f'{name:20} :  {age:02}')