
import matplotlib.pylab as pyl
#折线图plot,散点图plot,直方图 hist
import numpy as  npy
#生成随机数
data=npy.random.randint(1,20,500)#最小值,最大值,个数
print(data)

#生成正态分布的数据
data2=npy.random.normal(0,0.1,1000)#平均数,σ,个数
print(data2)


pyl.hist(data)
pyl.show()
#bar', 'barstacked', 'step', 'stepfilled
histtype="stepfilled"
histtype
sty=pyl.arange(5,25,1)#设置宽度,步长
pyl.hist(data,sty,)  #histtype="stepfilled  是默认的
pyl.show()
#
# pyl.subplot(2,3,2)#拆分纸图:行,列,当前区域
# pyl.show()
#
# #在纸图中绘制
# pyl.subplot(2,2,1)
# pyl.subplot(2,2,2)
# pyl.subplot(2,1,2)
# pyl.show()
#
#
# #在纸图中绘制
# pyl.subplot(2,2,1)
# x1=[1,2,3,4,5]
# y1=[2,7,9,3,7]
# pyl.plot(x1,y1)
# pyl.subplot(2,2,2)
# x2=[1,2,3,4,5]
# y2=[2,7,4,3,7]
# pyl.plot(x2,y2)
# pyl.subplot(2,1,2)
# x3=[1,2,3,4,5]
# y3=[2,7,4,3,7]
# pyl.plot(x3,y3)
# pyl.show()