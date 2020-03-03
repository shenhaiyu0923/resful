import os,sys,shutil,time
import gzip
import datetime
def download(path,d_time):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        shutil.rmtree(path)#删除老文件夹
        time.sleep(1)
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    os.getcwd()  # get current work direction.
    os.chdir(path)  # change direction.
    #downloadid="aws s3 sync s3://vova-vomkttest-evt/enrich-good/2019/09/18/03/ ."       2019/09/18/03
    downloadid = "aws s3 sync s3://vova-vomkttest-evt/enrich-good/"+d_time+"/ ."
    print(downloadid)
    os.system(downloadid)
def walk(*dirname_list):
    for i in dirname_list:
        for dirname, _, filenames in os.walk(i):
            for filename in filenames:
                yield os.path.join(dirname, filename)
    return


def open_gz(filename, encoding='utf8', is_gzip=None):
    if is_gzip is None:
        is_gzip = filename.endswith('.gz')
    if is_gzip:
        f = gzip.open(filename, 'rt', encoding=encoding)
    else:
        f = open(filename, encoding=encoding)
    return f


def main(keyword):
    dirname_list = [
            'e://good',
            ]
    for filename in walk(*dirname_list):
        with open_gz(filename) as r:
                s = r.readlines()
                for line in s:
                    s1 = line.find(keyword)
                    if s1 >= 0:
                        print(line.replace("\n", ""))

if __name__ == '__main__':
    newtime=datetime.datetime.utcnow().strftime('%Y/%m/%d/%H')
    download("E://good", newtime)  # 调用函数vivo
    print("{}的{}的文件将会下载至       E://good".format("vivo", newtime), end="\n")
    f = open('e://good/good.txt', 'w', encoding='utf-8')
    old = sys.stdout  # 将当前系统输出储存到临时变量
    sys.stdout = f    # 输出重定向到文件vivo
    #main("ft31022@tetx.com")
    main("00000000-0000-0000-0000-000000000000")
   # main("00000000-0000-0000-0000-000000000000")
    f.close()

