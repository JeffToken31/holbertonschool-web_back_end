#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
mongo_collection = client.logs.nginx

count_logs = mongo_collection.count_documents({})
print("{} logs".format(count_logs))
print("Methods:")

method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

get = mongo_collection.count_documents({"method": "GET"})
print("\tmethod GET: {}".format(get))
post = mongo_collection.count_documents({"method": "POST"})
print("\tmethod POST: {}".format(post))
put = mongo_collection.count_documents({"method": "PUT"})
print("\tmethod PUT: {}".format(put))
patch = mongo_collection.count_documents({"method": "PATCH"})
print("\tmethod PATCH: {}".format(patch))
delete = mongo_collection.count_documents({"method": "DELETE"})
print("\tmethod DELETE: {}".format(delete))


count_status = mongo_collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(count_status))
