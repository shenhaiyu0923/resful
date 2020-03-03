import numpy as np
import pandas as pd
a = np.array([[1,2,0,1],[1,6,9,55],[7,8,9,5]])#a为数组
print(a.T)  #矩阵
a = [1, 3, 5, 2, 4, 6]
b =  np.array(a)
a=np.array([3,2,3,4,5])
print(np.sort(a))
print (np.argsort(b)) # 正序输出
print (np.argsort(-b)) # 逆序输出
print (np.sort(b)) # 正序输出
a1=pd.Series([8,9,1,2])
a2=pd.Series([8,9,1,2],index=["one","two","three","four"])#指定索引
print(a1)
print(a2)
