import requests,hashlib,time,random,json
from pprint import pprint as print

class Youdao(object):
    def __init__(self,word):
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers ={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
                       'Cookie': 'OUTFOX_SEARCH_USER_ID=673979439@10.169.0.83; JSESSIONID=aaaD7CveG5Iou6Kli1qcx; OUTFOX_SEARCH_USER_ID_NCOO=1023587938.3051136; ___rl__test__cookies=1582984399944',
                       'Referer': 'http://fanyi.youdao.com/',
                        }
        self.formdata = None
        self.word = word



    def generate_formdata(self):
        '''
        ts: "" + (new Date).getTime()
        salt: ts + parseInt(10 * Math.random(), 10);
        sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        '''
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0,9))

        tempstr = "fanyideskweb" + self.word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"

        md5 = hashlib.md5()
        md5.update(tempstr.encode())
        sign = md5.hexdigest()
        self.formdata = {
           "i":self.word,
           "from":"AUTO",
           "to":"AUTO",
           "smartresult":"dict",
           "client":"fanyideskweb",
           "salt":salt,
           "sign":sign,
           "ts":ts,
           "bv":"31e52a7907cc3385be94e9,b647497a17",
           "doctype":"json",
           "version":"2.1",
           "keyfrom":"fanyi.web",
           "action":"FY_BY_REALTlME",
            "typoResult":False
        }
    def get_data(self):
        response = requests.post(self.url,data=self.formdata,headers=self.headers)
        return response.content.decode()

    def get_result(self,data):
        result=json.loads(data)
        result_2=result['translateResult'][0][0]['tgt']
        print(result_2)
    def run(self):
        # url
        # headers
        # formdata
        self.generate_formdata()
        # 发送请求，获取响应
        data = self.get_data()
        self.get_result(data)
        # 解析数据

if __name__ =='__main__':
    word = input('请输入单词')
    youdao=Youdao(word)
    youdao.run()