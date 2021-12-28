from tkinter import *

window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open",)
fileMenu.add_command(label="Save", )
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
# fileMenu.add_command(label="Open",)
# fileMenu.add_command(label="Save", )
window.mainloop()