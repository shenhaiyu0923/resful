from random import randint
import time


class Tiger:#定义类
    className = '老虎'
    def __init__(self,inWeight=200):
        self.weight = inWeight

    def roar(self):#实例方法
        print('我是老虎---wow!--体重减5斤')
        self.weight -= 5

    def feed(self,food):#喂食操作----实例
        if food == '肉':
            self.weight += 10
            print('喂食正确，体重增加10斤！')
        else:
            self.weight -= 10
            print('喂食错误，体重减少10斤！')

class Sheep:#定义类
    className = '羊'
    def __init__(self,inWeight=100):
        self.weight = inWeight

    def roar(self):#实例方法
        print('我是羊---mie!--体重减5斤')
        self.weight -= 5
    def feed(self,food):#喂食操作----实例
        if food == '草':
            self.weight += 10
            print('喂食正确，体重增加10斤！')
        else:
            self.weight -= 10
            print('喂食错误，体重减少10斤！')

class Room:#定义类的内容：属性  方法
    def __init__(self,inNum,inAnimal):# 编号  动物---实例属性
        self.num = inNum
        self.animal = inAnimal

#游戏初始化--房间初始化操作
roomList = []#[实例1，实例2]
for one in range(1,11):
    if randint(0,1) == 1:#双闭区间
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(one,ani)
    roomList.append(room)
#开始游戏   记录开始时间
totalweight=0#总体重
startTime = time.time()#单位s
while True:
    curTime = time.time()
    if curTime - startTime >= 10:
        print("时间到")
        for one in roomList:
            print("当前时间编号:{},房间的动物是{},总体重是{}".format(one.num,one.animal.className,one.animal.weight))
            totalweight +=one.animal.weight
        print("总体重是{}kg".format(totalweight))
        break

    roomNum=randint(1,10)#房间编号 int
    #去房间列表,对号入座
    roomObject=roomList[roomNum-1]#房间实例
    #接收是否敲门操作
    answer=input("当前房间编号是{},是否敲门y/n".format(roomNum)).strip()
    if answer =="y":
        roomObject.animal.roar()#该房间的动物叫
    food = input("请投喂食物:").strip()
    roomObject.animal.feed(food)




# t1 = Tiger()#创建实例---会自动调用构造方法___init__
# t2 = Tiger(100)#创建实例---

#创房间实例
# r1 = Room(5,t1)

# #描述下：房间5的动物的叫：房间.动物.叫
# r1.animal.roar()
#
# from random import randint#随机数
#
# # print(randint(0,2))# 0 1  2-----双闭区间


# #抽奖小操作
# nameList = ['xx','xxx']
# print(nameList[randint(0,len(nameList)-1)])


# t1.roar()#调用实例方法   实例.方法  不能是  类.方法
# t1.feed('草')
# print(t1.weight)
#
# print(t2.weight)

#时间操作
# import time
# # print(time.time())#1970到现在的秒数
#
#
#
# startTime = time.time()#开始
#
# while True:
#     curTime = time.time()
#     if curTime - startTime >= 120:
#         break
#


# t1 = Tiger()#创建实例
# t2 = Tiger()#创建实例
#
# print(t1.className)
# print(t2.className)
# print(Tiger.className)
#
# class SouTiger(Tiger):#减少代码量
#     def __init__(self,inHeight ):
#         Tiger.__init__(self,inWeight=200)
#         self.height = inHeight
#         print('SouTiger--初始化方法')
#     @staticmethod  #修饰下---只能修饰下面紧跟的一个
#     def static_roar():
#         print('子类----静态方法--叫')
#
# '''
# 关于继承：
#     1- 如果子类里面没有def __init__    会自动调用父类
#     2- 子类类名有自己的def ___init__  ,不会自动调用父类的，自己写父类的__init__
#     3- 可以自己增加子类的属性
#
#
# '''
# s1 = SouTiger(60)
# s1.static_roar()#方法重新--优先子类的
# # Tiger.static_roar()#
#
# super(SouTiger,s1).static_roar()#父类的
#
# print(s1.className)
# print(s1.weight)
# print(s1.height)





# print(t1)
