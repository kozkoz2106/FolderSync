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

repoButton = Button(root, text = "Select your repo", command=repoSelected).grid(row=0, column=0)
repoLocal = Button(root, text = "Select your local", command=localSelected).grid(row=0, column=2)

#repoButton.pack()
#repoLocal.pack()

root.mainloop()