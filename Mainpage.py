#!/user/bin/python3.5
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

"""
Code to set the size of the main window
"""
def center_window(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 1/2*screen_width
    height = 1/2*screen_height
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


"""
This code is for getting the directory
print function removed later
"""
def get_directory():
    dirname = filedialog.askdirectory()
    if dirname:
        directory.set(dirname) # sets the value of directory stringvar
def print_entry():
    print(directory.get())
def input_directory(status,name):
    directorylabel = ttk.Label(directoryframe, text=name)  # sets the name to the left of the entrybox
    directorylabel.pack(side=LEFT)
    text = status  # setting the blank as the default value of the entry box
    directory = StringVar(directoryframe)
    directory.set(text)
    entry = ttk.Entry(directoryframe,textvariable = directory)  # this is the textbox
    entry.pack(side=LEFT)
    return directory
"""
This code is for getting the altitude
print function removed late 
"""

def print_altitude():
    print(altitude.get())
def input_altitude(status,name):
    altitudelabel = ttk.Label(altitudeframe, text=name)
    altitudelabel.pack(side=LEFT)
    altitude = DoubleVar(altitudeframe)
    entry = ttk.Entry(altitudeframe,textvariable=altitude)
    entry.pack(side=LEFT)
    return altitude


def print_threshold():
    print(threshold.get())
def input_threshold(status,name):
    thresholdlabel = ttk.Label(thresholdframe, text=name)
    thresholdlabel.pack(side=LEFT)
    threshold = DoubleVar(thresholdframe)
    entry = ttk.Entry(thresholdframe,textvariable=threshold)
    entry.pack(side=LEFT)
    note = ttk.Label(thresholdframe,text="(Values should be between 0.0-1.0")
    note.pack(side=LEFT)
    return threshold


root = Tk()
root.title("EcoCensus")
center_window(root)
"""
This sections is to get the directory
"""
directoryframe = Frame(root) # frame to get the directory values
button = ttk.Button(directoryframe,text="Get Directory", command=get_directory)
button.pack(side=RIGHT)
getbutton = ttk.Button(root,text='Print entry text', command=print_entry)  # this gets removed later.
getbutton.pack(side=BOTTOM)
directory = input_directory("", "Directory")
directoryframe.pack(side=TOP)
"""
This section is to get the altitude
"""
altitudeframe = Frame(root)
altitude = input_altitude("", "Altitude")
altitudebutton = ttk.Button(root, text='Print Altitude value', command=print_altitude )  # this also gets removed late
altitudebutton.pack(side=BOTTOM)
altitudeframe.pack(side=TOP)

"""
This section is to get the prediction threshold 
"""
thresholdframe = Frame(root)
threshold = input_threshold("", "Prediction Threshold")
thresholdbutton = ttk.Button(root, text='Print Threshold value', command=print_threshold)  # this also gets removed
thresholdbutton.pack(side=BOTTOM)
thresholdframe.pack(side=TOP)

root.mainloop()
root.withdraw()


# split the ui into frames, top frame should be the predict button and variables

# side frame should be where you can see the images that have been predicted on

# then the other side frame should be the partioned image like how they have it in ecocensus

# learn how to switch ui tabs as well
