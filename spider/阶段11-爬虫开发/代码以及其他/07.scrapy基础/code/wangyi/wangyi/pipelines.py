# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient


class WangyiPipeline(object):

    def open_spider(self, spider):
        if spider.name == 'job':
            self.file = open('wangyi.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'job':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ',\n'

            self.file.write(str_data)

        return item

    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()


class WangyiSimplePipeline(object):

    def open_spider(self, spider):
        if spider.name == 'job_simple':
            self.file = open('wangyi_simple.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'job_simple':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ',\n'

            self.file.write(str_data)

        return item

    def close_spider(self, spider):
        if spider.name == 'job_simple':
            self.file.close()


class MongoPipeline(object):

    def open_spider(self, spider):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['itcast']
        self.col = self.db['wangyi']

    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)

        return item

    def close_spider(self, spider):
        self.client.close()
