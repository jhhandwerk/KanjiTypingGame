import random

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
              print("ok")
          else:
              print("you made a typing mistake")
        myinnerinnerfunc()
    myinnerfunc() 
function()

