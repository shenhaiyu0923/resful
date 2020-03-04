#coding:utf-8
import requests
from lxml import etree


class Tieba(object):

    def __init__(self, name):
        self.name = name
        self.url = 'http://tieba.baidu.com/f?kw={}'.format(self.name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
            # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) '
        }

    def get_data(self, url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def parse_list_page(self, data):
        """
            解析贴吧帖子列表页面的响应
        :param data: 帖子列表页面的响应
        :return: 帖子标题和链接列表 与 下一页url
        """
        data = data.decode().replace("<!--","").replace("-->","")
        html = etree.HTML(data)

        el_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # print(len(el_list))
        data_list = []
        for el in el_list:
            temp = {}

            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + el.xpath('./@href')[0]
            data_list.append(temp)
        try:
            next_url = 'http:' + html.xpath('//*[contains(text(),"下一页>")]/@href')[0]
        except:
            next_url = None

        return data_list, next_url

    def parse_detail_page(self, data):

        html = etree.HTML(data)

        return html.xpath('//*[contains(@id,"post_content_")]/img/@src')

    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送列表请求，获取响应
            list_page_data = self.get_data(next_url)

            # 解析列表页面的响应，提取帖子列表数据和下一页url
            data_list, next_url = self.parse_list_page(list_page_data)

            # 遍历帖子列表，获取每一个详细url
            for data in data_list:
                # 发起请求，获取到详情页面的响应
                data = self.get_data(data['link'])
                # 从响应中提取图片地址
                image_list = self.parse_detail_page(data)
                # 保存
                print(image_list)
            # 翻页&循环终止条件
            if next_url == None:
                break


if __name__ == '__main__':
    tieba = Tieba("传智播客")
    tieba.run()