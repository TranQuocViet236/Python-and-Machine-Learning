import os
from tkinter import *
from tkinter import filedialog

def openFile():
    path = "C:\\Users\\TGDD\\PycharmProjects\\pythonProject3"
    filepath = filedialog.askopenfile(initialdir=path,\
                                        title="Open file ok?",\
                                        filetypes=(("text files","*.txt"),\
                                      ("all files","*.*")))
    infor = filepath.read()
    print(infor)
    # print(filepath
    '''
    with open(filepath,"r") as file:
        print(file.read(),"r")
        file.close()
        '''
window = Tk()
openButton = Button(window,
                    text="Open File",
                    command=openFile)
openButton.pack()
window.mainloop()