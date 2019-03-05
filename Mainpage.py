#!/user/bin/python3.5
from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import filedialog
import image_partition as impa
import predictions as predict
from PIL import Image, ImageTk
import os, glob
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
This code is for displaying the partitioned image
"""
"""
def display_image():
    print("Trying to display dat shit")
    imageframe = Frame(predictframe)
    image = Image.open("C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG")
    photo = ImageTk.PhotoImage(image)
   # icon = ttk.PhotoImage(file = "C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG" )
    # displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
    label = ttk.Label(displayframe, image = photo)
    label.pack()
    imageframe.pack(side=TOP)
"""

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
print function removed later 
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
    predict.main(directory.get())


def input_threshold(status,name):
    thresholdlabel = Label(thresholdframe, text=name)
    thresholdlabel.pack(side=LEFT)
    threshold = DoubleVar(thresholdframe)
    entry = ttk.Entry(thresholdframe,textvariable=threshold)
    entry.pack(side=LEFT)
    note = ttk.Label(thresholdframe,text="(Values should be between 0.0-1.0)")
    note.pack(side=LEFT)
    return threshold


root = Tk()
root.title("EcoCensus")
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
center_window(root)
root.configure(background = '#9DE9AF')
predictframe = Frame(root)

"""
This section is to get the directory
"""
directoryframe = Frame(predictframe) # frame to get the directory values
button = ttk.Button(directoryframe,text="Get Directory", command=get_directory)
button.pack(side=RIGHT)
getbutton = ttk.Button(root,text='Print entry text', command=print_entry)  # this gets removed later.
getbutton.pack(side=BOTTOM)
directory = input_directory("", "Directory")
directoryframe.pack(side=TOP)
"""
This section is to get the altitude
"""
altitudeframe = Frame(predictframe)
altitude = input_altitude("", "Altitude")
altitudebutton = ttk.Button(root, text='Print Altitude value', command=print_altitude )  # this also gets removed late
altitudebutton.pack(side=BOTTOM)
altitudeframe.pack(side=TOP)

"""
This section is to get the prediction threshold 
"""
thresholdframe = Frame(predictframe)
threshold = input_threshold("", "Prediction Threshold")
thresholdbutton = ttk.Button(root, text='Print Threshold value', command=print_threshold)  # this also gets removed
thresholdbutton.pack(side=BOTTOM)
thresholdframe.pack(side=TOP)


def partition_predict():
    impa.main(directory.get())
    #add the directory that will read the newly created partition files.


predictbutton = ttk.Button(predictframe,text='Partition and Predict', command=partition_predict)
predictbutton.pack(side=TOP)

"""
This section is for displaying partitioned images
"""
"""
imageframe = Frame(predictframe)
image = Image.open("C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG")
photo = ImageTk.PhotoImage(image)
   # icon = ttk.PhotoImage(file = "C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG" )
    # displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
label = ttk.Label(root, image = photo)
label.pack()
imageframe.pack(side=TOP)
"""

#def display_image():
displayframe = Frame(root)
print("Trying to display dat shit")
imageframe = Frame(root)
"""
image = Image.open("C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG")
image = image.resize((800, 800), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
# icon = ttk.PhotoImage(file = "C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG" )
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
label = tk.Label(displayframe, image = photo,bg="white", borderwidth = 5, relief = 'solid')

label.pack()
"""
def positive_file(positive_files):
    print(positive_files)
    image_over = 0
    files = os.listdir(positive_files)
    old_label_image = None
    for f in files:
        if ".jpg" or ".JPG" in f:
            print(f)
            image1 = Image.open(positive_files + "/" + f)
            #root.geometry('%dx%d' % (image1.size[0], image1.size[1]))
            print(image1.size[0], image1.size[1])
            tkpi = ImageTk.PhotoImage(image1)
            label_image = tk.Label(root, image=tkpi)
            label_image.place(x=image_over, y= -15, width=image1.size[0], height=image1.size[1])
            root.title(f)

            #if old_label_image is not None:
                #old_label_image.destroy()
            old_label_image = image1
            image_over = image_over + old_label_image.size[0]

def display_images():
    positive_files = directory.get()+"/Positive"
    print(positive_files)
    positive_file(positive_files)


displaybutton = tk.Button(root, text='Display dat shit', command=display_images)
displaybutton.pack(side=BOTTOM)
displayframe.pack(side=BOTTOM)
imageframe.pack(side=TOP)
predictframe.pack()


root.mainloop()
root.withdraw()


# split the ui into frames, top frame should be the predict button and variables

# side frame should be where you can see the images that have been predicted on

# then the other side frame should be the partioned image like how they have it in ecocensus

# learn how to switch ui tabs as well
#TODO: Find all the .py files and connectors in the original Ecocensus project
#TODO: By connectors I mean things like