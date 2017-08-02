# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChewyItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    page=scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    rating = scrapy.Field()
    reviews_number = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    ingredient = scrapy.Field()
    
