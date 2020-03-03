# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    depart = scrapy.Field()
    category = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    num = scrapy.Field()
    date = scrapy.Field()

    duty = scrapy.Field()
    require = scrapy.Field()


class WangyiSimpleItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    depart = scrapy.Field()
    category = scrapy.Field()
    type = scrapy.Field()
    address = scrapy.Field()
    num = scrapy.Field()
    date = scrapy.Field()


