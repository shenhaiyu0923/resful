import pandas as  pd
import pymysql

print("----------------excel---------------")
#导入xecel文件
b=pd.read_excel("C:/study/aaa.xlsx")
print(b) #查询
print(b.describe())#统计
print("-----------------mysql--------------")
#导入mysql

conn=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="ming")

cur = conn.cursor()
sql="select * from yang"
cur.execute(sql)
k=pd.read_sql(sql,conn)
print(k)
print("---------------本地html----------------")

h=pd.read_html("C:/study/abc.html")
print(h)#list
print("----------------在线读取表格---------------")
m=pd.read_html("http://www.qinzhe.com/cn/baidu.html")  #在线读取表格,智能选择表格
print(m)


print("---------------文本----------------")
t=pd.read_csv("C:/abc.txt")#此方法已经淘汰,可以用read_csv读取txt文件
print(t)

print("-----------------CSV--------------")
i=pd.read_csv("C:/ab.csv")#导入,只导入数据
i.describe() #统计
print(i.describe())

#                 a           b           c
# count    5.000000    5.000000    5.000000
# mean   145.200000   93.200000  202.200000
# std    226.846203   81.263153  234.992979
# min     13.000000   33.000000   13.000000
# 25%     23.000000   46.000000   14.000000
# 50%     24.000000   67.000000   67.000000
# 75%    123.000000   86.000000  456.000000
# max    543.000000  234.000000  461.000000
i.sort_values(by="b")#按什么排序
print(i.sort_values(by="b"))



