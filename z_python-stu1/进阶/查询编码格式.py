import chardet
path = 'C:/study/123.txt'
data = open(path,'r')
print('-------------1--------------')
print(data.read())
print('------------2---------------')
print(data.tell())
print('-----------3----------------')
print(data)
print('------------4---------------')
data = open(path,'rb').read()
print(chardet.detect(data))

