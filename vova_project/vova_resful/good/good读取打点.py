with open('E://good/good.txt',encoding=('utf8')) as f1:
    cNames = f1.readlines()
    for i in range(0,len(cNames)):
        cNames[i] = str(i+1) + '.' + '' + cNames[i]
        print(cNames[i].strip())

#将处理过的cNames写入新的文件中
with open('./good','w+',encoding=('utf8')) as f2:
    f2.writelines(cNames)


