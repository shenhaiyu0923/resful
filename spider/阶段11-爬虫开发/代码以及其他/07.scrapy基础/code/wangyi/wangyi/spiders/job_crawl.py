# -*- coding: utf-8 -*-
import scrapy
# 链接提取器
from scrapy.linkextractors import LinkExtractor
# 爬虫类 规则
from scrapy.spiders import CrawlSpider, Rule


class JobCrawlSpider(CrawlSpider):
    name = 'job_crawl'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    # 链接处理规则
    rules = (
        # follow 决定是否继续在链接提取器提取的链接对应的响应中继续应用链接提取器，一般持续翻页的链接提取规则需要设置为true
        Rule(LinkExtractor(allow=r'\?currentPage=\d+$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        node_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        # print(len(node_list))

        # 遍历节点列表
        for num, node in enumerate(node_list):
            # 设置过滤条件，将目标节点获取出来
            if num % 2 == 0:
                item = {}

                item['name'] = node.xpath('./td[1]/a/text()').extract_first()
                # response.urljoin()用于拼接相对路径的url，可以理解成自动补全
                item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').extract_first())
                item['depart'] = node.xpath('./td[2]/text()').extract_first()
                item['category'] = node.xpath('./td[3]/text()').extract_first()
                item['type'] = node.xpath('./td[4]/text()').extract_first()
                item['address'] = node.xpath('./td[5]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()
                item['date'] = node.xpath('./td[7]/text()').extract_first()
                yield item

