import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testDB"]
mycol = mydb["testCollection"]

for x in mycol.find():
  print(x)
