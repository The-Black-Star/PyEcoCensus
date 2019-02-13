#!/user/bin/python3.5
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
def center_window(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 1/2*screen_width
    height = width
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def get_directory():
    dirname = filedialog.askdirectory()
    if dirname:
        directoy.set(dirname)

def input_file(status,name):
    optionframe = Frame(root)
    optionlabel = Label(optionframe,text=name)
    optionlabel.pack(side=LEFT)
    text = status
    directory = StringVar(root)
    directory.set(text)
    entry = Entry(optionframe,textvariable = directory)
    entry.pack(side=LEFT)
    optionframe.pack()
    return entry, directory

def print_entry():
    print (directory.get())

root = Tk()
root.title("EcoCensus")
center_window(root)

button = Button(root,text="ask directory", command = get_directory)
button.pack(side=LEFT)
getbutton = Button(root,text='Print entry text')#, command = print_entry())
getbutton.pack(side = BOTTOM)


#TODO: Find all the .py files and connectors in the original Ecocensus project
#TODO: By connectors I mean things like

entry,directory = input_file("your directory here","directory")

root.mainloop()
root.withdraw()
