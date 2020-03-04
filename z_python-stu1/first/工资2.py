# -*-coding:utf-8-*-
rfileDir='c:/study/gongsi.txt'
wfileDir='c:/study/xie1.txt'
with open(rfileDir,'r') as rFile,open(wfileDir,'w') as wFile:
    #3- 获取每一行内容 fo.read().splitlines()----去换行符---返回是list
    lines = rFile.read().splitlines()
    for line in lines:
        #4- 分割开名字跟工资
        if line.count(';') == 1:
            temp = line.split(';')# ['name: Jack'   ,   ' salary:  12000']
            if temp[0].count(':') == 1 and temp[1].count(':') == 1:
                name = temp[0].split(':')[1].strip()
                salary = temp[1].split(':')[1].strip()#str--暂时不能进行算术运算
                print(salary)
                if salary.isdigit():
                    salary = int(salary)
                    #5- 计算+排版
                    info = 'name:{:>6};  salary:{:>6};  tax:{:>6};  income:{:>6}'.format(name,salary,int(salary*0.1),int(salary*0.9))
                else:
                    info = 'this line salary is not digit'
            else:
                info = 'this line : is error'
        else:
            info = 'this line ; is error'
        wFile.write(info + '\n')
        print(info+'\n')