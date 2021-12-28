from tkinter import *

window = Tk()
frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.place(x=0,y=0)
Button(frame, text="w", font=("San",25), width=3).pack(side=TOP)
Button(frame, text="A", font=("San",25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("San",25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("San",25), width=3).pack(side=LEFT)

window.mainloop()