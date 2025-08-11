#!/usr/bin/env python3
"""
    Update all topics of a school document based on the name
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.my_db.school


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name
    """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
