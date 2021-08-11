import random
import pymongo
import time
import dns
from pymongo.results import UpdateResult

#DB variables
myclient = pymongo.MongoClient('mongodb+srv://Rogue1:97HeeHee@cluster0.oqryr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
mydb = myclient['typingTest']
mycol = mydb["typingTest.typingTestCollection"] 
#function variables
myKanjiList = ["雨", "自ら", "山","森", "川","海", "木","水", "上","下", "田"]
myYomiList = ["あめ","みずから","やま","もり","かわ","うみ","き","みず","うえ","した","だ"]
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

def function():
    randomNum = random.randint(0, 2)
    x = myKanjiList[randomNum] 
    print("The letter is % s" % (x))
    def myinnerfunc():
        y = input("type the letter above:")
        def myinnerinnerfunc():
          if y == myYomiList[randomNum]:
              print("ok")
              if randomNum == 0:
                  def ameAmeFureFure():
                      mydict = { 
                         "雨": 1, 
                         "time": time.time()
                         }
                      x = mycol.insert_one(mydict)
                  ameAmeFureFure()
              elif randomNum == 1:
                  def mizuKara():
                      mydict = { 
                         "自ら": 1, 
                         "time": time.time() }
                      x = mycol.insert_one(mydict)
                  mizuKara()
              elif randomNum == 2:
                  def jyonaYama():
                    mydict = { 
                         "山": 1, 
                         "time": time.time() }
                    x = mycol.insert_one(mydict)
                  jyonaYama()              
          else:
              def no():
                mydict = { 
                    "count": 1, 
                    "question": [randomNum], 
                    "answer": 0 }
                x = mycol.insert_one(mydict)
              no()
              print("you made a typing mistake")
        myinnerinnerfunc()
    myinnerfunc() 
function()

