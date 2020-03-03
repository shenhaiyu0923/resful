import os

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
file = 'E:\\good\\Test'
mkdir(file)  # 调用函数
os.getcwd() #get current work direction.
os.chdir('E:\\good\\Test') #change direction.
with open("123.txt","r") as rfile:
    os.system("aws s3 sync s3://vova-vomkttest-evt/enrich-good/2019/09/18/03/ .")
print("==========")