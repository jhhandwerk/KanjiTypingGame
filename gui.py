from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clciked a button!")
    myLabel.pack()


myButton = Button(root, text="click me!", pady=50, command=myClick)
myButton.pack()

root.mainloop()