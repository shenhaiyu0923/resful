#coding:utf-8
import requests
import json
#import sys

class King(object):

    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
        }
        self.data = {
        'f': 'auto',
        't': 'auto',
        'w': word
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content

    def parse_data(self, data):
        dict_data = json.loads(data)
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    def run(self):
        # 构思爬取思路
        # url
        # headers
        # formdata
        # 发送请求获取响应
        data = self.get_data()
        # print(data)

        # 解析响应
        self.parse_data(data)

if __name__ == '__main__':
    #king = King("人生苦短，及时行乐")好
    word = input('请输入:')
    king = King(word)
    king.run()