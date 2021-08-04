import random
import pymongo
import time
import dns

#DB variables
myclient = pymongo.MongoClient('mongodb+srv://Rogue1:97HeeHee@cluster0.oqryr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
mydb = myclient['typingTest']
mycol = mydb["typingTest.typingTestCollection"] 

for x in mycol.find():
  print(x)