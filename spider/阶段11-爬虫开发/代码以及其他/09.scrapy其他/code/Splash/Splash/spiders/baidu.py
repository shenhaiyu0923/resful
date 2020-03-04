# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=python']

    def parse(self, response):
        with open('baidu.html','wb')as f:
            f.write(response.body)
