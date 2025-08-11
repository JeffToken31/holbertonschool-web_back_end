#!/usr/bin/env python3
"""
Fonction to list all documents in a collection
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.my_db.school

def list_all(mongo_collection):
    """
    List all documents in collection else return empty list
    """
    result = []

    for document in mongo_collection.find():
        result.append(document)
    return result