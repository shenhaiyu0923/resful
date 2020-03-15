import time
import hashlib
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
    return md5Encryption

a={'c':123,'b':234}
encryptionRules(a)