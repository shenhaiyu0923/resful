str='01 23456789'
print(str[1:2+3])  #左含右不含

a=[1,2,3,4,5,6,7,8,9,10,11,]
print(a[2:7])

li=[1,1,2,2,3,4,5,5,6]
print(set(li))
print(set([1,1,2,2,3,3]))

ll=[1,1,2,2,3,4,5,5,6]
m=[]
for one  in ll:
    if one not in m:
        m.append(one)
print(m)


