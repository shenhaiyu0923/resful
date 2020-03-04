# a=[1,2,5,1,2,6,3]
# b=[4,6,2,4,1,6]
# print(a+b)
# c=list(set(a+b))
# print(c)
# print(list(reversed(c)))

def reverseStr(source):
    # 将字符串中的每个字符放入列表中
    tmp = [c for c in source]
    # 列表倒序
    tmp.reverse()
    return tmp
print (reverseStr('hello'))
