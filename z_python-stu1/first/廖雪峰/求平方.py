def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

a=power(5, 3)
print(a)
print('请输入x')
