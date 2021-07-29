import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['testDB']
mycol = mydb["testCollection"]

mydict = { "name": "Spock", "address": "Enterprise" }

x = mycol.insert_one(mydict)

print(x.inserted_id)
