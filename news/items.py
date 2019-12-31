# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,MapCompose,Join,Compose

def revert_time(values):
    if values:
        format_time = datetime.datetime.strptime(values,"%Y-%m-%d %H:%M:%S")
        return format_time
    else:
        return ""

class NewsItemloader(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(NewsItemloader):
    content_out = Compose(Join(), lambda s: s.strip())

class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    #content = scrapy.Field(output_processor=Join(""))
    content = scrapy.Field()
    source = scrapy.Field()
    #times = scrapy.Field(input_processor=MapCompose(revert_time))
    times = scrapy.Field()
    website = scrapy.Field()
    url = scrapy.Field()
