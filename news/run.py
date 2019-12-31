__author__ = 'luohua139'

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_config,get_project_settings
from news.spiders.unvnews import UnvnewsSpider
import pymongo
def run():
    setting = dict(get_project_settings())
    process  = CrawlerProcess(get_project_settings())
    process.crawl(UnvnewsSpider)
    process.start()



if __name__ == '__main__':
    run()