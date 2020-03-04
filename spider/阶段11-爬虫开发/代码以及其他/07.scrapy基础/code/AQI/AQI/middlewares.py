# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
from scrapy import signals


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        url = request.url

        if 'daydata' in url:
            driver = webdriver.Chrome()

            driver.get(url)
            time.sleep(3)
            data = driver.page_source

            driver.close()

            # 创建响应对象
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)

            return res
