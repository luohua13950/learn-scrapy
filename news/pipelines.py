# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import pymongo
class NewsPipeline(object):
    #def __init__(self,host,port,user,passwd,db,collections,uri):
    def __init__(self,uri,db,collections):
        self.uri = uri
        self.db = db
        self.collections = collections

    @classmethod
    def from_crawler(cls,crawler):
        setting = dict(get_project_settings())
        uri = setting.get("MONGODB_URI")
        host = setting.get("MONGODB_HOST")
        port = setting.get("MONGODB_PORT")
        user = setting.get("MONGODB_USER")
        passwd = setting.get("MONGODB_PASSWORD")
        return cls(uri,crawler.settings.get('MONGODB_DBNAME'),crawler.settings.get('MONGODB_COLLECTIONS'))

    def open_spider(self,spider):
        #self.mongo = pymongo.MongoClient(self.host,self.port,username=self.user,password=self.passwd)
        self.client = pymongo.MongoClient(self.uri)
        self.dbs = self.client.news
        #self.dbs.authenticate("", "")
        self.collection = self.dbs.new

    def process_item(self, item, spider):
        #self.collection.insert_one(dict(item))
        print(item)
        return item

    def close_spider(self,spider):
        self.client.close()