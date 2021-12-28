from tkinter import *

count = 0
window = Tk()
window.title("Love programming <3")
# window.geometry("275x183")
# photo = PhotoImage(file="heart.jpg")
photo = PhotoImage(file="./Basic_GUI/Data/images.png")
window.geometry("420x420")
def love():
    global  count
    if count % 2==0:
        print("Love you!")
    count +=1
button = Button(window,
                text="Double tap to open my heart!",
                font=("Times new roman",20),
                fg= "green",
                bg= "black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom",
                command= love
                )
button.pack()


if __name__ == "__main__":
    window.mainloop()