import random
import pymongo
import time
import dns

#DB variables
myclient = pymongo.MongoClient('mongodb+srv://Rogue1:97HeeHee@cluster0.oqryr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
mydb = myclient['typingTest']
mycol = mydb["typingTest.typingTestCollection"] 

myTable = [
    {   "kanji_id":0,
        "kanji":"雨",
        "value":0
    },
    {
        "kanji_id":1,
        "kanji":"",
        "value":0
    },
    {
        "kanji_id":2,
        "kanji":"自ら",
        "value":2
    },
    {
        "kanji_id":3,
        "kanji":"山",
        "value":2
    },
    {
        "kanji_id":4,
        "kanji":"森",
        "value":6
    },
    {
        "kanji_id":5,
        "kanji":"川",
        "value":13
    },
    {
        "kanji_id":6,
        "kanji":"海",
        "value":0
    },
    {
        "kanji_id":7,
        "kanji":"木",
        "value":4
    },
    {
        "kanji_id":8,
        "kanji":"上",
        "value":2
    },
    {
        "kanji_id":9,
        "kanji":"下",
        "value":3
    },
    {
        "kanji_id":10,
        "kanji":"田",
        "value":10
    },
]
myTable2 = [
    {
        "池": 0
    },
    {
        "石": 0
    },
    {
        "鳥": 0
    }
]
x = mycol.insert_many(myTable)
print(x.inserted_ids)


