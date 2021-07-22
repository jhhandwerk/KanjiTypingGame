import random

mylist = ["あ", "い", "う","え", "お","か", "き","く", "け","こ", "さ"]
def function():
    x = mylist[random.randint(0, 10)] 
    print("The letter is % s" % (x))
    def myinnerfunc():
        y = input("type the letter above:")
        def myinnerinnerfunc():
          if y == x:
              print("ok")
          else:
              print("you made a typing mistake")
        myinnerinnerfunc()
    myinnerfunc() 
function()

