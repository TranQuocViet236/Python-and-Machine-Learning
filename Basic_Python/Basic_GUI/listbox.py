from tkinter import *


def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    print("You have order: ")
    for i in food:
        print(i)
    # print("You have ordered " + str(listbox.get(listbox.curselection())))
    listbox.config(height=listbox.size())


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())
    print("Added")


def delete():
    for i in listbox.curselection():
        listbox.delete(i)
    listbox.config(height=listbox.size())
    print("Deleted")


window = Tk()
# window.geometry("420x420")
listbox = Listbox(window,
                  bg= "#f7ffde",
                  font=("Arial", 30),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()
listbox.insert(0,"pizaa")
listbox.insert(1,"bread")
listbox.insert(2,"noodles")
listbox.insert(3,"hamburger")
listbox.config(height=listbox.size())
submit_button =  Button(window,
                        text="Submit",
                        command=submit
                        )
submit_button.pack()
add_button =  Button(window,
                        text=" Add ",
                        command=add
                        )
add_button.pack()
delete_button =  Button(window,
                        text=" Delete ",
                        command=delete
                        )
delete_button.pack()
entry_box = Entry(window
                  )
entry_box.pack()


if __name__ == "__main__":
    window.mainloop()