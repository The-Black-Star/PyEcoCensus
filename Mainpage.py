#!/user/bin/python3.5
from tkinter import *
#from tkinter.ttk import *
import tkinter as tk
#import tkinter.ttk as ttk
def center_window(root, width,height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root = Tk()
root.title("EcoCensus")
center_window(root,1000,800)

#TODO: Find all the .py files and connectors in the original Ecocensus project
#TODO: By connectors I mean things like

root.mainloop()