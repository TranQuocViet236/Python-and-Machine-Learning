from tkinter import *
from tkinter import messagebox
def click():
   messagebox.showinfo(title="A",message="B")

window = Tk()
click_button = Button(window,
                      text="Click me!",
                      command=click
                      )
click_button.pack()
if __name__ == "__main__":
    window.mainloop()