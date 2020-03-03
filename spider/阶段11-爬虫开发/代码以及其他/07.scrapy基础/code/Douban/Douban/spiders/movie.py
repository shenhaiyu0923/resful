# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.request.headers['User-Agent'])

        movie_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]')

        # print(len(movie_list))

        for movie in movie_list:
            item = DoubanItem()

            item['name'] = movie.xpath('./div[1]/a/span[1]/text()').extract_first()

            yield item

        next_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if next_url != None:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url)