# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash.request import SplashRequest

class BaiduWsSpider(scrapy.Spider):
    name = 'baidu_ws'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=python']

    def start_requests(self):

        url = self.start_urls[0]

        yield SplashRequest(
            url=url,
            callback=self.parse,
            args={'wait': 10},  # 最大超时时间，单位：秒
            endpoint='render.html'
        )

    def parse(self, response):
        with open('baidu_with_splash.html','wb')as f:
            f.write(response.body)
