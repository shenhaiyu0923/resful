from hashlib import md5
import base64

def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    m5=new_md5.hexdigest()

    #再次使用base64加密
    #p = m5.encode("utf-8")
    #p = base64.b64encode(p)  # 被编码的参数必须是二进制数据
    #return m5,p
    return m5
# 调用
if __name__ == '__main__':
    print(encrypt_md5('111111'))