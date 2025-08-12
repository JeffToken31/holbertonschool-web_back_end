#!/usr/bin/env python3
"""
Improve code by adding the top 10 of the most present IPs in the collection nginx
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    mongo_collection = client.logs.nginx

    count_logs = mongo_collection.count_documents({})
    print("{} logs".format(count_logs))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count_method = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count_method))

    count_status = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(count_status))

    print("IPs:")
    ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("{}: {}".format(ip["_id"], ip["count"]))