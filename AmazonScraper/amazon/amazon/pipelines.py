# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class AmazonPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(  # creates the connections
            'localhost',
            27017
        )

        db = self.conn['monitors']  # creates a database
        self.collection = db['MonitorData']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
