fileDir = r'C:\\study\stu.txt'
def putInfoToDict(fileName):
    resDict = {}#保存结果
    #1- 打开文件
    with open(fileName) as fo:
        lines = fo.read().splitlines()
        for line in lines:
            line  = line.replace('(','').replace(')','').replace('\t','').replace("'",'').replace(';',',')
            temp  = line.split(',')
            checkTime = temp[0].strip()
            lessonId = int(temp[1].strip())
            userId = int(temp[2].strip())
            infoDict = {'lessonid': lessonId,'checkintime':checkTime}
            #统计
            if userId not in resDict:#增加---键值对
                resDict[userId] = []
            resDict[userId].append(infoDict)#增加信息

            # if userId not in resDict:
            #     resDict[userId] = [infoDict]
            # else:
            #     resDict[userId].append(infoDict)  # 增加信息


    return resDict

res = putInfoToDict(fileDir)
print(res)
#完美打印
import pprint
pprint.pprint(res)
