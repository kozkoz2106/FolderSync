from tkinter import *

root = Tk()

def repoSelected():
    repotxt = Label(root, text = "File 'repo' selected")
    repotxt.pack()

def localSelected():
    localtxt = Label(root, text = "File 'local' selected")
    localtxt.pack()

myLabel = Label(root, text = "Welcome to Gitfile!")
myLabel.pack()

repoButton = Button(root, text = "Select your source", command=repoSelected)
repoLocal = Button(root, text = "Select your destination", command=localSelected)

repoButton.pack()
repoLocal.pack()

root.mainloop()