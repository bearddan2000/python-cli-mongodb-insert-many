from pymongo import MongoClient
import pprint

client = MongoClient('db', 27017)

db = client.test

print("[INFO] Before Insert empty collection")
pprint.pprint(db.list_collection_names())

shiv = [{"name": "shiv"}, {"name": "short sword"}]

collection = db.weapon

collection.insert_many(shiv)

print("[INFO] After Insert 1 collection")
pprint.pprint(db.list_collection_names())

print("[INFO] Select all")
for item in collection.find():
    pprint.pprint(item)
