from tkinter import *

root = Tk()
e = Entry(root, width = 40)
e.pack()

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()


myButton = Button(root, text="Enter your name", pady=50, command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()