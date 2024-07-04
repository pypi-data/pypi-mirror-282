# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient('mongodb://root:02OUXQd9Z@dds-bp1bd6b8bc0f3704-pub.mongodb.rds.aliyuncs.com:3717')
db = client['crawl_data']  # 替换为你的数据库名称
collection = db['crawl_brand']  # 替换为你的集合名称


def add_one_data(info, table_name='crawl_brand', collection_name='crawl_data'):
    client[collection_name][table_name].insert_one(info)
