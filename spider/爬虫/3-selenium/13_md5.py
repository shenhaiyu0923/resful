'827ccb0eea8a706c4c34a16891f84e7b'
import hashlib


def get_token():
    md5str = "111111"
    md5 = hashlib.md5()
    #使用md5对象里的update方法md5转换
    md5.update(md5str.encode("utf-8"))
    result = md5.hexdigest()
    print(result)

    return result

get_token()


string1 = "thisismytest".encode()

out1 = hashlib.sha256(string1)
out1=out1.hexdigest()
print (out1)

