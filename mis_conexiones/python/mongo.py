from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tienda']
collection = db['producto']

for document in collection.find():
    print(document)
