# 引入模块
import os
def mkdir(path):
    # 判断目录是否存在
    # 存在：True
    # 不存在：False
    folder = os.path.exists(path)
    # 判断结果
    if not folder:
        # 如果不存在，则创建新目录
        os.makedirs(path)
        print('-----创建成功-----')
    else:
        # 如果目录已存在，则不创建，提示目录已存在
        print(path + '目录已存在')
path = 'd:\\xxoo\\test'
mkdir(path)

