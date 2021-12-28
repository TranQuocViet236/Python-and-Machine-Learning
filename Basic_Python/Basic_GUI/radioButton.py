from tkinter import *
from PIL import ImageTk, Image


window = Tk()
food = ["pizza","bread","noodle"]
pizzaImage = PhotoImage(file="Data/pizza.png")
breadImage = PhotoImage(file="Data/bread1.png")
noodlesImage = ImageTk.PhotoImage(Image.open("noodles1.png"))
foodImage = [pizzaImage, breadImage, noodlesImage]
x = IntVar()
for i in range(len(food)):
    radio_button = Radiobutton(window,
                           font="Arial",
                           text = food[i],
                            variable=x,
                           value=i,
                            padx=25,
                               image=foodImage[i]
                               )
    radio_button.pack(anchor=W)
if __name__ == "__main__":
    window.mainloop()