import os
import sys
import gzip


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
    f = open('e://good/ios.txt', 'w', encoding='utf-8')
    old = sys.stdout  # 将当前系统输出储存到临时变量
    sys.stdout = f    # 输出重定向到文件
    main('ios')
    f.close()
