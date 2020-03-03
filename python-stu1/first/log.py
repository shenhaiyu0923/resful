
# 记录各种类型的文件的数量统计，存储格式如下
# [['jpg',4566],['json',4566]]
fileLenTable = []

# 根据文件类型找到记录对象,进行累加
def putRecordToTable(fileType,fileLen):
    for one in fileLenTable:
        if one[0] == fileType:
            one[1] += fileLen
            return

    # 没有找到,创建一个记录元素
    fileLenTable.append([fileType,fileLen])
    return


for line in log.split('\n'):
    if line.strip() == '':
        continue

    parts = line.split('\t')
    name,size = parts[:2]

    ext = name.split('.')[-1]

    putRecordToTable(ext,int(size))


print(fileLenTable)