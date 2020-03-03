'''
a=open('d:/file1.txt','w')   写文档
a1='fefeqferafdsa'
a.write(a1)
a.close()
'''

b= open('d:/file2.txt', 'r',encoding='UTF-8')  #读文件
while True:
    line=b.readline()
    if len(line)==0:
        break
    print(line)
b.close()









