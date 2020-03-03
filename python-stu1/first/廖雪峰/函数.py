def playfootball(a):
    print(a)  # 这是参数
    print('分成两队')
    print('向对方握手')
    print('开始踢球')

print("--------------")
print(playfootball)  # 对应一个函数对象
playfootball('张三');  # 调用对象，要注意缩进，不然无效
print("--------------")

def fun1():
    print(123);


print('-----------------');
fun1();
print('你好');
