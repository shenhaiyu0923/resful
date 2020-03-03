fileDir='C:/study/1234.txt'
fo=open(fileDir).read()
print(fo)
linesList=fo.split('\n')
del linesList[0],linesList[-1]#删除首行尾行
#print(linesList)
resList  =[]#保存结果[[类型1，大小1]，[类型2，大小2]，]
#1- 获取每一行的类型、大小---每一行，列以\t分割
del linesList[0],linesList[-1]#去list前后的空字符串
#2- 对每一行进行遍历
for line in linesList:#line---每一行内容
    temp = line.split('\t')#返回是List
    fileType = temp[0].split('.')[1].strip()
    fileSize = int(temp[1].strip())#累加需要int---强制转换

    #3- 统计类型大小--------明天早上的课程--字典来统计--4行代码
    inFlag = False#初始化状态---变量----每一行获取到类型、大小的时候,inflag = false
    #判断该行类型是不是在结果列表里面
        #1- 在-----累加大小
        #2- 不在----新增
    #新增的前提是--该类型不存在
    # 保存结果[[类型1，大小1]，[类型2，大小2]，]
    #4- 判断存不存在
    for one in resList:#one 取 子列表  --[类型1，大小1]
        if fileType == one[0]:#存在该类型---累加
            one[1] += fileSize#累加
            inFlag = True#说明存在该类型
            break#结束判断存在操作

    if  inFlag== False:#新增
        resList.append([fileType,fileSize])


print(resList)
