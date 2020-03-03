inList = [8,3,0,9,1]
def my_sort(inList):
    newList = []#保存结果
    while len(inList) >0:#取最小值次数
        minData = min(inList)#找一个最小值
        newList.append(minData)#新增结果列表
        inList.remove(minData)#删掉最小值
    return newList


print(my_sort(inList))
