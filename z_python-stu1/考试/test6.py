str = '''
name   = '小明'
age    = 16
height = 170
'''
print(str.replace('\n','&').replace('name','姓名').replace('age','年龄').\
    replace('height','身高').replace(' ','').replace("'",'')[1:-1])


