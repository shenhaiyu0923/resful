fileDir='C:/study/1234.txt'
fo=open(fileDir).read()
print(fo)
linesList=fo.split('\n')
del linesList[0],linesList[-1]
#print(linesList)
resList=[]
for line in linesList:
    temp=line.split('\t')
    fileType=temp[0].split('.')[1].strip()
    fileSize=int(temp[1].strip())
    print(fileType,fileSize)#
    inFlag=False
    for one in resList:
        if fileType ==one[0]:
            one[1]+=fileSize
            inFlag = True
            break
    if inFlag==False:
        resList.append([fileType,fileSize])
print("------------------------")
print(resList)