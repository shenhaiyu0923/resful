import numpy
import pandas as  pd
import matplotlib.pylab as pyl

data=pd.read_csv("C:/ab2.csv")#导入,只导入数据
print("--------------查询几行几列(12,3)----------------------")
print(data.shape)#查询几行几列(12,3)
print("------------------统计分析------------------")
print(data.describe())#统计分析
print("------------------第1行,第3列  表头不算------------------")
print(data.values[0][2])#第1行,第3列  表头不算
print("-----------------第一行-------------------")
print(data.values[0])  #第一行
print("----------------转置后--------------------")
data2=data.T  #转置
print(data2) #转置后
x=data2.values[2]
y=data2.values[1]
print("----------------转置后X--------------------")
print(x)
print("----------------转置后Y--------------------")
print(y)
pyl.plot(x,y,"or")#红色散点图
pyl.show()