import random
import pymongo
import time

#DB variables
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['testDB']
mycol = mydb["KanjiTest"]
#function variables
myKanjiList = ["雨", "自ら", "山","森", "川","海", "木","水", "上","下", "田"]
myYomiList = ["あめ","みずら","やま","もり","かわ","うみ","き","みず","うえ","した","だ"]
def function():
    randomNum = random.randint(0, 10)
    x = myKanjiList[randomNum] 
    print("The letter is % s" % (x))
    def myinnerfunc():
        y = input("type the letter above:")
        def myinnerinnerfunc():
          if y == myYomiList[randomNum]:
              def yes():
                mydict = { "count": 1, "question": [randomNum], "answer": 1, "time": time.time() }
                x = mycol.insert_one(mydict)
              yes() 
              print("ok")
          else:
              def no():
                mydict = { "count": 1, "question": [randomNum], "answer": 0 }
                x = mycol.insert_one(mydict)
              no()
              print("you made a typing mistake")
        myinnerinnerfunc()
    myinnerfunc() 
function()

