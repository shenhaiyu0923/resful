# 仍然引入随机数模块, 拿到一个随机数列表
# import random
# def random_10(amount):
#     li = []
#     for i in range(amount):
#         s = random.randint(0, 10)
#         li.append(s)
#     print(li)
#
#     return li
# lst = sorted(random_10(10))
lst=[1,2,3,4,15,16,23,34,45,46]
# 定义一个递归函数
def func(n, lst, left=0, right=None):
    if right == None:
        right = len(lst) - 1
    if left <= right:
        mid = (left + right) // 2
        if n < lst[mid]:
            right = mid - 1
        elif n > lst[mid]:
            left = mid + 1
        else:
            print("你输入的数在这个列表中,它的位置{}\n".format(mid))
            return True
        return func(n, lst, left, right)
    else:
        print("你输入的数不在这个列表中\n")
        return False

while 1:
    n = int(input("请输入你要查找的数:"))
    func(n, lst)