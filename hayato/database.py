# -*- coding: utf-8 -*-

from datetime import datetime
from pymongo import DESCENDING, MongoClient
from bson.objectid import ObjectId

class Database:

    client = None
    db = None

    def __init__(self):
        if Database.client is None:
            Database.client = MongoClient('127.0.0.1')
            Database.db = Database.client.sankei
        else:
            print "already database connected."

    def news(self, id):
        news = Database.db.news
        return  news.find_one({'_id':ObjectId(id)})

    def news_category_count(self):
        news = Database.db.news
        return list(
            news.aggregate([{'$group':{'_id':'$category','count':{'$sum':1}}}])
            )

    def dictionary(self, category, id):
        dictionary = Database.db[category]
        return  dictionary.find_one({'_id':ObjectId(id)})

    def dictionary_category_news(self, category, id):
        dictionary = Database.db[category]
        news = Database.db.news
        dic = dictionary.find_one({'_id':ObjectId(id)})
        its = []
        for it in dic['news_ids']:
            its.append(news.find_one({'_id':it}))
        return its

    def dictionary_category_nouns(self, category):
        dictionary = Database.db[category]
        words = dictionary.count()
        word = dictionary.find(
            { '$and': [
                {'feature':{'$nin': self._nin_features()}}, 
                {'$where':"this.noun.length > 1"},
                {'count':{'$gte':100}}
                ]
            }).sort('count',DESCENDING)
        return word


    def news_date(self, date, category=""):
        start_date = datetime(date.year,date.month,date.day,0,0,0)
        end_date = datetime(date.year,date.month,date.day,23,59,59)
        news = Database.db.news
        if category == "":
            return news.find({"date":{"$gte":start_date, "$lte":end_date}}).sort("date", DESCENDING)
        else:
            return news.find({"category": category, "date":{"$gte":start_date, "$lte":end_date}}).sort("date", DESCENDING)

    def _nin_features(self):
        return [
            "形容動詞語幹接尾",
            "ナイ形容詞語幹",
            "形容動詞語幹",
            "接続詞的",
            "サ変接続",
            "副詞可能",
            "接尾",
            "数",
            ]
