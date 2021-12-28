from tkinter import *


def submit():
    name = entry.get()
    print("Your love is priceless! "+name)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()
window.title("Ask your love <3")
entry = Entry(window,
              font=("Arial",20),
              bg = "#e3ceeb",
              show="*"
              )
# entry.insert(0,"Hello Bro Code")
entry.pack(side=LEFT)
submit_button = Button(window,
                text="Ask",
                font=("Arial",20),
                bg="#e3ceeb",
                # fg="#e3ceeb",
                command=submit
                       )
submit_button.pack(side=RIGHT)
delete_button=Button(window,
                     text= "Delete",
                     font=("Arial",20),
                     bg="#e3ceeb",
                     command=delete
                     )
delete_button.pack(side=LEFT)
backspace_button= Button(window,
                         text="Backspace",
                         font=("Arial",20),
                         bg="#e3ceeb",
                         command = backspace
                         )
backspace_button.pack(side=LEFT)


if __name__ == "__main__":
    window.mainloop()