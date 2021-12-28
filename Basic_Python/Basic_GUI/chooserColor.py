from tkinter import colorchooser
from tkinter import *


def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)

window = Tk()
window.geometry("420x420")
clickButton = Button(window,
                     text="Color",
                     command=click,
                    )
clickButton.pack()


if __name__ == "__main__":
    window.mainloop()
