# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# cralspider 经常应用于数据在一个页面的情况
class TencentCrawlSpider(CrawlSpider):
    name = 'tencent_crawl'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    # 链接提取规则
    rules = (
        # LinkExtractor 用于设置链接提取规则，一般用allow参数，接收正则表达式
        # follow参数决定是否在链接提取器提取的链接对应的响应中继续应用链接提取器提取链接
        # 使用Rule类生成链接提取规则

        # 设置详情页面链接提取规则
        #Rule(LinkExtractor(allow=r'position_detail.php\?id=\d+&keyword=&tid=0&lid=0'), callback='parse_item'),

        Rule(LinkExtractor(allow=r'position_detail.php\?&start=\d+#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        print('python21',response.url)
        return item
