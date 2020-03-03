# -*- coding: utf-8 -*-
import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        pass
