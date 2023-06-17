from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4sggwrz.mongodb.net/"

client = MongoClient(url)

db = client.pytech

collection = db.list_collection_names()

print("-- Pytech Collection List --")
print(collection)