# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem
# scrapy crawl itcast  --nolog
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    # def parse(self, response):
    #     with open('itcast1.html','wb')as f:
    #         # scrapy中response.body是bytes类型的源码
    #         f.write(response.body)
    def parse(self, response):
#         print(response.url)
#         print(response.request.url)
#         print(response.request.headers)
#         print(response.headers)
#         print(response.status)
#         获取所有讲师节点列表
        node_list = response.xpath('//div[@class="li_txt"]')
        #print(len(node_list))

        # 遍历讲师节点列表，从没一个节点中抽取数据
        for node in node_list:
            #item = {}
            item = MyspiderItem()
            # 节点调用xpath方法之后获得一个选择器对象列表,调用选择器对象的extract()方法可以从选择器对象中提取数据，
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first() #返回其中第一条
            item['desc'] = node.xpath('./p/text()').extract_first()
            # item['desc'] = node.xpath('./p/text()')[0].extract() #把一个列表中都返回,(建议使用)
            #print(item)
            yield item


