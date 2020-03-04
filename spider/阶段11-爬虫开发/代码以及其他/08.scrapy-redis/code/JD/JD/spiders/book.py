# -*- coding: utf-8 -*-
import scrapy
from JD.items import JdItem
import json

# ----1 导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider


# ----2 继承分布式爬虫类
class BookSpider(RedisSpider):
    name = 'book'

    # ----3 注销start_urls&allowed_domains
    # # 修改允许的域
    # allowed_domains = ['jd.com', 'p.3.cn']
    # # 修改起始的url
    # start_urls = ['https://book.jd.com/booksort.html']

    # ----4 设置redis-key
    redis_key = 'py21'

    # ----5 设置__init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(BookSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取所有图书大分类节点列表
        big_node_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt/a')

        for big_node in big_node_list[:1]:

            big_category = big_node.xpath('./text()').extract_first()
            big_category_link = response.urljoin(big_node.xpath('./@href').extract_first())

            # 获取所有图书小分类节点列表
            small_node_list = big_node.xpath('../following-sibling::dd[1]/em/a')

            for small_node in small_node_list[:1]:
                temp = {}

                temp['big_category'] = big_category
                temp['big_category_link'] = big_category_link
                temp['small_category'] = small_node.xpath('./text()').extract_first()
                temp['small_category_link'] = response.urljoin(small_node.xpath('./@href').extract_first())

                # 模拟点击小分类链接
                yield scrapy.Request(
                    url=temp['small_category_link'],
                    callback=self.parse_book_list,
                    meta={"py21": temp}
                )


    def parse_book_list(self, response):
        temp = response.meta['py21']

        book_list = response.xpath('//*[@id="plist"]/ul/li/div')
        # print(len(book_list))

        for book in book_list:

            item = JdItem()

            item['big_category'] = temp['big_category']
            item['big_category_link'] = temp['big_category_link']
            item['small_category'] = temp['small_category']
            item['small_category_link'] = temp['small_category_link']

            item['bookname'] = book.xpath('./div[3]/a/em/text()|./div/div[2]/div[2]/div[3]/a/em/text()').extract_first().strip()
            item['author'] = book.xpath('./div[4]/span[1]/span/a/text()|./div/div[2]/div[2]/div[4]/span[1]/span[1]/a/text()').extract_first().strip()
            item['link'] = book.xpath('./div[1]/a/@href|./div/div[2]/div[2]/div[1]/a/@href').extract_first()

            # 获取图书编号
            skuid = book.xpath('.//@data-sku').extract_first()
            # skuid = book.xpath('./@data-sku').extract_first()
            # print("skuid:",skuid)
            # 拼接图书价格低至
            pri_url = 'https://p.3.cn/prices/mgets?skuIds=J_' + skuid
            yield scrapy.Request(url=pri_url,callback=self.parse_price,meta={'meta_1':item})

    def parse_price(self, response):
        item = response.meta['meta_1']

        dict_data = json.loads(response.body)

        item['price'] = dict_data[0]['p']
        yield item
