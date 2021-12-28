from tkinter import *
from tkinter import filedialog


def save():
    pathfile = filedialog.asksaveasfile(initialdir="C:\\Users\\TGDD\\PycharmProjects\\pythonProject3",
                                        defaultextension=".txt",
                                        filetypes= [("text file",".txt")])
    filetext = str(text.get("1.0",END))
    # print(file)
    if pathfile is None:
        return
    pathfile.write(filetext)
    pathfile.close()
window = Tk()
submitButton = Button(window,
                      text="submit",
                      command=save
                      )
submitButton.pack()
text = Text(window,)

text.pack()
window.mainloop()