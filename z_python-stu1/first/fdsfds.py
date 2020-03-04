fileDir="C://study/stu.txt"
def putInfoDict(fileDir):
    resDict={}#用于保存结果
    #-打开文件
    #{'checkintime': '2017-03-13 12:02:27', 'lessonid': 271}
    with open(fileDir) as  fo:
        lines=fo.read().splitlines() #按行读取
        print(lines)
        for line in lines:
            line = line.replace('(','').replace(')','').replace('\t','').replace("'",'').replace(';',",")
            temp=line.split(',')#以什么为分割
            checkTime=temp[0].strip()#strip默认去除第一个空格
            lessonId=int(temp[1].strip())
            userId=int(temp[2].strip())
            infoDict={"lessonid":lessonId,"checkintime":checkTime}
            if userId not in resDict:
                resDict[userId]=[]
            resDict[userId].append(infoDict)#增加信息
    return resDict
res=putInfoDict(fileDir)
print(res)
import pprint
pprint.pprint(res)