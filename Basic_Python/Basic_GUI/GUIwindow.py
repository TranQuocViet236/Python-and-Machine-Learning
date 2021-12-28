from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Bro code first GUI window")
photo = PhotoImage(file="./Basic_GUI/Data/180px-FC_Barcelona_logo.svg.png")
window.iconphoto(True, photo)
window.config(background="#363240")

if __name__ == "__main__":
    window.mainloop()
