#!/usr/bin/env python3
"""
Return a list of students sorted by score
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.my_db.pymongo


def top_students(mongo_collection):
    """
    Return a list of students sorted by score
    """
    return mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ])
