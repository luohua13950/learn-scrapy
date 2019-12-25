# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem,NewsItemloader
from scrapy.link import Link
from scrapy.loader import ItemLoader

from scrapy.loader.processors import TakeFirst, Join, Compose

#'mongodb://luohua:123456@118.25.181.239:27017'
class UnvnewsSpider(CrawlSpider):
    name = 'unvnews'
    allowed_domains = ['news.china.com']
    start_urls = ['http://news.china.com/domestic/']

    rules = (
        Rule(LinkExtractor(allow=r'domestic/.*.html', restrict_xpaths="//div[@class='bd defList']"),
             callback='parse_item', follow=True, process_request="process_req", process_links="process_link"),
        # Rule(LinkExtractor(allow=r'',))
    )


    def parse_item(self, response):
        loders = NewsItemloader(item = NewsItem(),response=response)
        loders.add_xpath("title","//h1[@id='chan_newsTitle']/text()")
        loders.add_xpath("content","//div[@id='chan_newsDetail']//p/text()")
        loders.add_xpath("source","//span[@class='source']/a/text()")
        loders.add_xpath("times","//div[@class='chan_newsInfo_source']/span[@class='time']/text()")
        loders.add_value("website","中华网")
        print(loders.load_item())
        yield loders.load_item()


    def process_link(self, link):
        return link[0:2]


    def process_req(self, request):
        return request