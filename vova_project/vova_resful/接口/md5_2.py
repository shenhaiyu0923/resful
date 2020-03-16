import time
import hashlib
from pprint import pprint as print
def encryptionRules(dirt):
    md5Name = ''
    #dirt['req_time'] = '1578712943'
    keyList = sorted(dirt.keys())
    for i in keyList:
        md5Name = md5Name + str(dirt[i])
    md5Name = md5Name + 'vovaapiv5'
    print(md5Name)
    md5Encryption = hashlib.md5(md5Name.encode('gb2312')).hexdigest()
    print(md5Encryption)
    dirt["sign"]=md5Encryption
    return dirt


parame = {
    "timezone": "Asia/Shanghai",
    "access_token": "",
    "s": "2",
    "uid": "0",
    "imei": "540000000045036",
    "imsi": "46007",
    "uuid": "340fee311994e386",
    "other": ";;0;46007;;;1;GMT+08:00;1;0",
    "version": "2.65.0",
    "currency": "EUR",
    "is_new_user": "0",
    "brand_country_code": "CN",
    "country_code": "FR",
    "req_time": "1584084992",
    "sign": ""
}

md5Encryption=encryptionRules(parame)
print(md5Encryption)