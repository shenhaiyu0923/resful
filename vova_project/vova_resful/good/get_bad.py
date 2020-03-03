import os
import sys
import gzip,shutil,time
import datetime

import json
import re
import base64

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
    downloadid = "aws s3 sync s3://vova-vomkttest-evt/enrich-bad/"+d_time+"/ ."
                # "aws s3 sync s3://vova-vomkttest-evt/enrich-bad/2019/12/24/11/ ."
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


def iter_jsons(f, is_jsonlines=True):
    if is_jsonlines:
        for i in f:
            yield json.loads(i)
    else:
        s = f.read()
        pos = 0
        while True:
            try:
                yield json.loads(s[pos:])
                break
            except json.JSONDecodeError as e:
                yield json.loads(s[pos:pos+e.pos])
                pos += e.pos
    return 


SUPPORT_RAW_CONTEXT = False
if SUPPORT_RAW_CONTEXT:
    data_pattern = re.compile(br'"data":(\[.+\}\])\}')
else:
    data_pattern = re.compile(br'"data":(\[[^][]+])')


def get_data_as_json(bLine):
    result = data_pattern.findall(bLine)    
    if not result:
        print('!!!can not find "data"!!!')
        return
    if len(result) > 1:
        print('!!!too many "data"!!!')
        return
    result = result[0]
    try:
        return json.loads(result)
    except json.decoder.JSONDecodeError:
        print('!!!invalid json for "data"!!!')
        return


def b64d(x):
    if isinstance(x, bytes):
        x = x.decode()
    x = x.rstrip('=')
    if '/' in x:
        x = x.replace('\\', '')
    tail = len(x) % 4
    if tail == 3:
        x += '='
    elif tail == 2:
        x += '=='
    elif tail == 1:
        x = x[:-1]
    if '-' in x or '_' in x:
        result = base64.b64decode(x, '-_', validate=True)
    else:
        result = base64.b64decode(x, validate=True)
    return result


def pretty_json(x):
    try:
        return json.dumps(json.loads(x), indent=2)
    except:
        if isinstance(x, str):
            x = x.encode('utf8')
        return b"!!!invalid json!!!" + x


def main():
    dirname_list = [
            r'e://bad',
            ]
    for filename in walk(*dirname_list):
        with open_gz(filename) as f:
            for i in iter_jsons(f):
                errors = i['errors']
                i = base64.b64decode(i['line'], validate=True,)
                # if not (True
                #         and b'vova_h5' in i.lower()
                #         ):
                #     continue
                print(errors)
                print(i)
                data = get_data_as_json(i)
                if not data:
                    continue
                for n, j in enumerate(data):
                    print('[%d]' % (n+1))
                    print(json.dumps(j, indent=2))  # ;continue
                    for k in ('cx', 'ue_px'):
                        if k in j:
                            print('%s=\n%s' % (k, pretty_json(b64d(j[k]))))
                    if SUPPORT_RAW_CONTEXT:
                        for k in ('co', 'ue_pr'):
                            if k in j:
                                print('%s=\n%s' % (k, pretty_json(j[k])))


if __name__ == '__main__':
    newtime=datetime.datetime.utcnow().strftime('%Y/%m/%d/%H')
    download("E://bad", newtime)  # 调用函数vivo
    f = open('e://bad/bad.txt', 'w', encoding='utf-8')
    old = sys.stdout
    sys.stdout = f
    main()
    f.close()
   

#   aws s3 sync s3://vova-vomkttest-evt/enrich-bad/2019/11/22/16/ .