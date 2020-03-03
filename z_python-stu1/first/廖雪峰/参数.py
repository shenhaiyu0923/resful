def foo2(a, b):
    print((a * 3 + b * 5) / 23)


foo2(3, 4);
foo2(a=3, b=4);
foo2(b=4, a=3);  # 可置换顺序
foo2(3, b=4);


# foo2(a=3,4);   这么写错误，有一个指定名字了，后面的也要指定

def product(*numbers):
    if len(numbers) == 0:
        raise TypeError
    else:
        sum = 1
    for n in numbers:
        sum = sum * n
    return sum


# 测试
print('product(5)=', product(5))
print('product(5,6)=', product(5, 6))
print('product(5,6,7)=', product(5, 6, 7))
print('product(5,6,7,9)=', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败')
elif product(5, 6) != 30:
    print('测试失败')
elif product(5, 6, 7) != 210:
    print('测试失败')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败')
else:
    try:
        product()
        print('测试失败')
    except TypeError:
        print('测试成功')
