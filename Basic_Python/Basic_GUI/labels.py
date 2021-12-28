from tkinter import *

window = Tk()
window.title("Bro code")
photo = PhotoImage(file="Data/180px-FC_Barcelona_logo.svg.png")
window.iconphoto(True,photo)
label = Label(window,
              text = "Bro, do you even code?",
              font = ("Times new roman",40,"bold"),
              fg ="green",
              bg = "yellow",
              image=photo,
              compound="bottom"

                )
label.pack()
if __name__ == "__main__":
    window.mainloop()