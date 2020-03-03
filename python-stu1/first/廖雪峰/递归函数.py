def sumFun(max):
  if max <=10 and max >= 0:
    return max+ sumFun(int(max) - 1)
  else:
    return 0
print(sumFun(10))

print(sum([x for x in range(11)]))

a=[1,2,3,4,5,6,7,8,9,10,11,12]

