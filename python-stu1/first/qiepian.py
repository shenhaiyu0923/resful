# info='a old lady come in, the name is mary, level 94454'
# def getName(a):
#     return a.split('the name is ')[1].split(',')[0].strip()
# print(getName(info))


#zhangsan,23;lisi,4;
info=input('please enter message:')#
temList=info.split(';')
del temList[-1]
for one in temList:
    name,age=one.split(',')
    print('{:<20}:   {:0>2};'.format(name,age))