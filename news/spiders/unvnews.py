# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem,NewsItemloader,ChinaLoader
from scrapy.link import Link
from scrapy.loader import ItemLoader
from scrapy.utils.project import get_config,get_project_settings
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
    def __init__(self, *a, **kw):
        self.rule_dict = self.load_rule()
        self.allowed_domains = ['news.china.com']
        self.start_urls = ['http://news.china.com/domestic/']
        super(UnvnewsSpider, self).__init__(*a, **kw)

    def parse_item(self, response):
        loders = ChinaLoader(item = NewsItem(),response=response)
        # loders.add_xpath("title","//h1[@id='chan_newsTitle']/text()")
        # loders.add_xpath("content","//div[@id='chan_newsDetail']//p/text()")
        # loders.add_xpath("source","//span[@class='source']/a/text()")
        # loders.add_xpath("times","//div[@class='chan_newsInfo_source']/span[@class='time']/text()")
        loders.add_value("url",response.url)
        for name,_rule in self.rule_dict["item"].items():
            rule = _rule.get("rule","")
            method = _rule.get("method","")
            re = _rule.get("re","")
            if all(rule,method):
                for r,m in zip(rule,method):
                    if m == "add_xpath":
                        loders.add_xpath(name,r)
                    elif m == "add_value":
                        loders.add_value(name,r)
                    elif m == "add_css":
                        loders.add_css(name,r)
            else:
                continue
        yield loders.load_item()

    def process_link(self, link):
        return link[0:2]


    def process_req(self, request,response):
        return request

    @classmethod
    def load_rule(cls):
        import json
        import os
        path = os.getcwd()
        #with open(os.path.join(path,"utils","conf.txt"),"r",encoding="utf-8") as rule:
        with open(".\\utils\\conf.text","r",encoding="utf-8") as rule:
            rules = json.load(rule)
        return rules

if __name__ == '__main__':
    link = "aaa"
    import os
    setting = dict(get_config("..\\utils\\config.txt"))
    print(setting.get("item"))