def atest(num,list1):
    n=num%len(list1)
    list2=[]
    for i in range(-n, 0):
        list2.append(list1[i])
    for i in range(len(list1) - n):
        list2.append(list1[i])
    print(list2)


while True:
    a = input('请输入循环次数：')
    atest(int(a),[1,2,3,4,5,6,7])


