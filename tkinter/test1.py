from tkinter import *

root = Tk()

ent = Entry(root)
ent.pack()

def myclick():
    mylabel = Label(root, text = "look i clicked")
    mylabel.pack()

mybutton = Button(root, text = "idi naxui", command = myclick)
mybutton.pack()

root.mainloop()