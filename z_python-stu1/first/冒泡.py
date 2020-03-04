alist1 = [1, 5, 0, 9, 2]

for i in range(0, len(alist1) - 1):  # 0 ~4 ----  0 1 2 3--取最大值的次数
    for j in range(0, len(alist1) - i - 1):
        # 只是交换的次数，但要不要交换取决于   相邻值的大小  temp
        if alist1[j] > alist1[j + 1]:
            alist1[j], alist1[j + 1] = alist1[j + 1], alist1[j]
print(alist1)
print("--------------------------------------------------------")
#第二种方法
alist = [8,1,0,2]
alist.sort(reverse=True)
print(alist)
