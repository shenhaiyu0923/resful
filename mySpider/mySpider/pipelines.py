# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyspiderPipeline(object):
    def __init__(self):
        self.file = open('itcast.json', 'w')
    def process_item(self, item, spider):
        #默认使用管道后就将数据返回给引擎
        #print(item)
        # 在scrapy框架中将item对象强转成字典类型的数据
        dict_data = dict(item)
        str_data = json.dumps(dict_data, ensure_ascii=True) + ',\n'
        self.file.write(str_data)
        return item
