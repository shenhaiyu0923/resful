import matplotlib.pylab as pyl
#折线图plot,散点图plot,直方图 hist
import numpy as  npy
#折线图
x=[1,2,3,4,8]
y= [1,6,4,7,9]
'''

c青色,r红色,m品红,g绿色,b蓝色,y黄色,k黑色,w白色

'''
pyl.plot(x,y,"r")#(X轴数据,y轴数据,展现形式)
pyl.show()
print("-----------------------------------")
#散点图
pyl.plot(x,y)#(X数据,y数据,展现形式)
'''
o散点图
'''
pyl.plot(x,y,"o")
pyl.show()

pyl.plot(x,y,"or")#红色散点图
pyl.show()

'''
线条
-直线   --虚线  -.-.形式  :细小虚线

'''
pyl.plot(x,y,"-")
pyl.show()
pyl.plot(x,y,"-.-.")
pyl.show()
pyl.plot(x,y,":")
pyl.show()
pyl.plot(x,y,"--")
pyl.show()

'''
点样式,
s 方形  h六角形  H六角形  *星形 +加号 X x形  d, D菱形  ,p五角形
'''
pyl.plot(x,y,"H")
pyl.show()


#  标题
x= [1,2,3,4,8]
y= [1,6,4,7,8]
x2=[2,5,6,8,9]
y2=[4,4,6,7,8]
pyl.plot(x,y)
pyl.plot(x2,y2)  #多条线段
pyl.title("title")
pyl.xlabel("time")
pyl.ylabel("name")
pyl.xlim(0,10)  #量程
pyl.ylim(1,10)
pyl.show()
