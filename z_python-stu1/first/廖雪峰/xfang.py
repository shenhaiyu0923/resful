import math

def quadratic(a,b,c):

    if not isinstance(a,(int,float)):

        raise TypeError('bad operand type')

    if not isinstance(b,(int,float)):

        raise TypeError('bad operand type')

    if not isinstance(c,(int,float)):

        raise TypeError('bad operand type')

    if b*b-4*a*c < 0:

        print=('此方程组无解')

        return

    if a==0 and b==0:

        print=('此方程组无解')

        return

    if a==0 and b!=0:

        x=-c/b

        return x

    if b*b-4*a*c>=0:

        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    return x1,x2

#测试
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')