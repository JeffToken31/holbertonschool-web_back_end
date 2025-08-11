#!/usr/bin/env python3
"""
    Return a list containing a specific topic
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.my_db.school


def schools_by_topic(mongo_collection, topic):
    """
    Return a list containing a specific topic
    """
    return mongo_collection.find({"topics": topic})
