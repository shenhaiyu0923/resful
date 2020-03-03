#对象的方法
#count
a='231fadfasa'.count('fa');#查询有多少个fa
print('count的方法=',a)#查询有多少个fa

#endwith  检查字符串是否以指定字符串结尾   是的话返回ture
#startwith  检查字符串是否以指定字符串开始
a1='12312313dsdadsadsa'.endswith('sa');
print('endwith的方法',a1)
#find  返回指定的字符串在字符串中出现的位置
# 如果不存在返回-1，如果有重复的显示第一个位置
a2='dsa,dsfsd,afda,daxcggfh'.find('da');
print(a2)
#表示从第五个字符开始找
a3='dfh,gfd,ior,oiwenriw'.find(',',5);
print(a3)
#截取姓名
#  001 come in, the name is jack,level 9;
a4='001 come in, the name is jack,level 9;'
p0=a4.find('the name is ');
p1=p0+len('the name is ');
p2=a4.find(',',p1);
print(a4[p1:p2])
#isalpha检查是否都是字母
#isdigit检查是否都是数字
a5='231321'.isdigit();
print(a5)
print(111111111111111111)
#join可以将字符串拼接起来
g=['sad','gdf','rtr']
g1=';'.join(g)#用；分开
print(g1)  #sad;gdf;rtr
#split可以将字符串分开
g2='13213232323'
g3=g2.split("2")#用2分割
print(g3)  #['13', '13', '3', '3', '3']
#以分隔符查找
a6='001 come in, the name is jack,level 9;'
a7=a6.split('the name is ')[1];
print(a7)  #jack,level 9;
a8=a7.split(',')[0];
print(a8)#jack

#大小写转换lower全转为小写，upper全转为大写
d1='dsfdadaAfdsAF'.lower();
d11='sfdsfdgdf'.capitalize();#首字符大写
print(d1)
print(d11)#Sfdsfdgdf

#replace替换字符串
d2='tom is a dog'
d3=d2.replace("dog","pig")
d4=d2.replace('dog','') #换成空字符串
print(d3)
print(d4)

#strip 将前置和后置空格去掉
#lstrip将前置空格去掉
#rstrip将后置空格去掉
a3='  dfsfds sfsd'
print(a3.lstrip())

#list列表对象常用方法
b1=[343];
b1.append('234')   #添加字符串
print(b1)
#insert 插入到指定位置
b2=[12,22,43,45,56]
b2.insert(2,44)
print(b2)
#删除元素del，pop
b3=[112,222,433,435,536];
del b3[2];  #根据下标删除
print(b3)
b4=b3.pop(3);
print(b4)  #使用pop方法删除会打印出被删掉的数据，根据下标删除
print(b3)#[112, 222, 435]
#remove 如果有多个相同的，只能删除第一个，根据元素删除，不是根据下标
b3.remove(112)
print('remove方法',b3)#[222, 435]