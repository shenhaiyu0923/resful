# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):

    def __init__(self):
        self.file = open('itcast.json', 'w')

    # 默认调用process_item方法，该方法用于定义如何处理数据
    def process_item(self, item, spider):
        # 在scrapy框架中将item对象强转成字典类型的数据
        dict_data = dict(item)

        str_data = json.dumps(dict_data, ensure_ascii=False) + ',\n'

        self.file.write(str_data)

        return item

    def __del__(self):
        self.file.close()