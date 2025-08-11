#!/usr/bin/env python3
"""
Insert datas in collection and return id of thisn
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.my_db.school


def insert_school(mongo_collection, **kwargs):
    """
    Insert datas in collection and return id of this
    """
    return mongo_collection.insert_one(kwargs).inserted_id
