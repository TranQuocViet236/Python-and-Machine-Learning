from tkinter import *

window = Tk()
def display():
    if x.get()==1:
        print("You agree!")
    else:
        print("You dont agree!")

x = IntVar()
photo = PhotoImage(file="./Basic_GUI/Data/images.png")
check_box = Checkbutton(window,
                        text="I agree with something!",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=display,
                        # padx = 20,
                        # pady=40,
                        image=photo,
                        compound = "bottom"
                        )
check_box.pack()

if __name__ =="__main__":
    window.mainloop()