# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

# class ItcastSpider(scrapy.Spider):
#     name = 'itcast'
#     # 设置允许的域，也就爬虫能够爬取的域名范围，允许的域默认不带子域名信息
#     allowed_domains = ['itcast.cn']
#     # 设置起始的url
#     start_urls = ['http://itcast.cn/']
#
#     # parse方法默认解析起始URL对应的响应
#     def parse(self, response):
#         with open('itcast1.html','wb')as f:
#             # scrapy中response.body是bytes类型的源码
#             f.write(response.body)
#         with open('itcast2.html','w')as f:
#             # scrapy中response.text是str类型的源码
#             f.write(response.text)
#         print(response.url)
#         print(response.request.url)
#         print(response.request.headers)
#         print(response.headers)
#         print(response.status)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 2 检查修改允许的域
    allowed_domains = ['itcast.cn']
    # 1 修改起始的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    # 3 编写parse方法，设计爬取过程
    def parse(self, response):
        # 获取所有讲师节点列表
        node_list = response.xpath('/html/body/div[1]/div[5]/div[2]/div/ul/li/div[2]')
        # print(len(node_list))

        data_list = []
        # 遍历讲师节点列表，从没一个节点中抽取数据
        for node in node_list:

            # item = {}
            item = MyspiderItem()

            # 节点调用xpath方法之后获得一个选择器对象列表,调用选择器对象的extract()方法可以从选择器对象中提取数据，
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['desc'] = node.xpath('./p/text()').extract_first()

            # 如果xpath得到的结果列表中只有一个数据，那么就可以使用extract_first(),否则使用extract（）
            # 在spiders文件中不适用return返回数据，使用yield进行替代
            # data_list.append(item)
            yield item
        # return data_list





