#!/user/bin/python3.5
from tkinter import *
from tkinter.ttk import *
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import filedialog
import image_partition as impa
import predictions as predict
import imageReader as imread
from PIL import Image, ImageTk, ExifTags
import os, glob

import time
import shutil
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
Constants for setting button and label columns
"""
entrycol = 1
labelcol = entrycol



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


def input_directory(status, name):
    directorylabel = ttk.Label(root, text=name)  # sets the name to the left of the entrybox
    directorylabel.grid(column = labelcol, row = 0, sticky = W)
    #directorylabel.pack(side=LEFT)
    text = status  # setting the blank as the default value of the entry box
    directory = StringVar(root)
    directory.set(text)
    entry = ttk.Entry(root, textvariable = directory)  # this is the textbox
    #entry.pack(side=LEFT)
    entry.grid(column = entrycol, row = 0, sticky = E)
    return directory


"""
This code is for getting the altitude
print function removed later 
"""


def print_altitude():
    print(altitude.get())


def input_altitude(status, name):
    altitudelabel = ttk.Label(root, text=name)
    #altitudelabel.pack(side=LEFT)
    altitudelabel.grid(column = labelcol, row = 1, sticky = W)
    altitude = DoubleVar(root)
    entry = ttk.Entry(root,textvariable=altitude)
    #entry.pack(side=LEFT)
    entry.grid(column = entrycol, row = 1, sticky= E)
    return altitude


def print_threshold():
    print(threshold.get())
    #predict.main(directory.get())


def input_threshold(status, name):
    thresholdlabel = Label(root, text=name)
    # thresholdlabel.pack(side=LEFT)
    thresholdlabel.grid(column = labelcol, row = 2, sticky = W)
    threshold = DoubleVar(root)
    entry = ttk.Entry(root, textvariable=threshold)
    #entry.pack(side=LEFT)
    entry.grid(column = entrycol, row = 2, sticky = E)
    note = ttk.Label(root, text="(Values should be between 0.0-1.0)")
    #note.pack(side=LEFT)
    note.grid(column = entrycol+1, row = 2, sticky = W)
    return threshold

#Icons made by "https://www.flaticon.com/authors/roundicons from "https://www.flaticon.com/" ,www.flaticon.com, is licensed by http://creativecommons.org/licenses/by/3.0/ Creative Commons BY 3.0
root = Tk()
root.title("EcoCensus")
root.iconbitmap("leaf_tss_icon.ico")
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
center_window(root)
root.configure(background = '#dbe9d8')
root.columnconfigure(0, weight =1)
root.columnconfigure(1, weight =1)
root.columnconfigure(2, weight =1)
root.rowconfigure(3,weight = 2)
displayframe = tk.Frame(root,bg="#dbe9d8")
displayframe.configure(bg="#dbe9d8")
displayframe.grid(columnspan = 2,column = 0, row = 3, sticky= N+S+E+W)
displayframe.grid_rowconfigure(0, weight=1)
displayframe.grid_columnconfigure(0, weight=1)


#root.columnconfigure()
#predictframe = Frame(root)

"""
This section is to get the directory
"""
#directoryframe = Frame(predictframe) # frame to get the directory values
button = tk.Button(root, text="Get Directory", command=get_directory, bg = "#f2efe8")
button.grid(column = entrycol+1, sticky = W)
#button.pack(side=RIGHT)
#getbutton = tk.Button(root, text='Print entry text', command=print_entry, bg = "#f2efe8")  # this gets removed later.
#getbutton.grid(column=entrycol, row=10)
#getbutton.pack(side=BOTTOM)
directory = input_directory("", "Directory")
#directoryframe.pack(side=TOP)
"""
This section is to get the altitude
"""
#altitudeframe = Frame(predictframe)
altitude = input_altitude("", "Altitude")
#altitudebutton = tk.Button(root, text='Print Altitude value', command=print_altitude, bg = "#f2efe8" )  # this also gets removed late
#altitudebutton.grid(column=entrycol, row=11)
#altitudebutton.pack(side=BOTTOM)
#altitudeframe.pack(side=TOP)

"""
This section is to get the prediction threshold 
"""
#thresholdframe = Frame(predictframe)
threshold = input_threshold("", "Prediction Threshold")
#thresholdbutton = tk.Button(root, text='Print Threshold value', command=print_threshold, bg = "#f2efe8")  # this also gets removed
#thresholdbutton.grid(column=entrycol, row=12)
#thresholdbutton.pack(side=BOTTOM)
#thresholdframe.pack(side=TOP)


"""
This section is for using the model
"""
def partition_predict():
    # calls image_partition.py, passing selected directory
    impa.main(directory.get())
    predict.main(directory.get(), threshold.get())
    imread.main(directory.get(), altitude.get())
    partdirectory = os.path.dirname(directory.get() + '/Partitions/')
    negdirectory = os.path.dirname(directory.get() + "/Negative/")
    posdirectory = os.path.dirname(directory.get() + "/Positive/")
    os.rmdir(partdirectory)
"""
    shutil.rmtree(negdirectory)
    now = time.gmtime()
    os.rename(posdirectory,directory.get() +"/Positive"+ time.strftime("%Y-%m-%d_%H-%M-%S", now))
    # add the directory that will read the newly created partition files.
"""

predictbutton = tk.Button(root,text='Partition and Predict', command=partition_predict, bg = "#f2efe8")
predictbutton.grid(column = entrycol, row = 4, sticky = E)
#predictbutton.pack(side=TOP)

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
#displayframe = Frame(root)
#print("Trying to display dat shit")
#imageframe = Frame(root)
"""
image = Image.open("C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG")
image = image.resize((800, 800), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
# icon = ttk.PhotoImage(file = "C:\\Users\\Lindsey\\PycharmProjects\\untitled\\Images\\example.JPG" )
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
label = tk.Label(displayframe, image = photo,bg="white", borderwidth = 5, relief = 'solid')

label.pack()
"""
def display_images():
    positive_files = directory.get()+"/Positive"
    print(positive_files)

    """Canvas dimensions and placement"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 1 / 2 * root.winfo_screenwidth()
    height = 1 / 2 * root.winfo_screenheight()
    x = (root.winfo_screenwidth() / 2) - (width / 2)
    y = (root.winfo_screenheight() / 2) - (height / 2)
    displaycanvas = Canvas(displayframe, width=(width - (height / 2)), height=height, bg="#dbe9d8")
    xscroll = Scrollbar(displayframe,orient=HORIZONTAL)
    xscroll.grid( column = 0, row = 4, sticky = E+W)
    #yscroll = Scrollbar(displayframe,orient = VERTICAL)
    #yscroll.grid( row = 4,column = 2, sticky = N+S)

   # displaycanvas.geometry('%dx%d+%d+%d' % (width, height, x, y))
    displaycanvas.grid(column = 0, row = 0, sticky= N+S+E+W)
    xscroll.config(command = displaycanvas.xview)
    #yscroll.config(command = displaycanvas.yview)
    displaycanvas.config(scrollregion=[0,0,(width - (height / 2))*4, height *2])
    displaycanvas.config(xscrollcommand=xscroll.set)
    displaycanvas.config(scrollregion = displaycanvas.bbox(ALL))

    image_over = 0
    ychange = -15
    files = os.listdir(positive_files)
    print(files)
    row_num = 5
    col_num = 0
    old_label_image = None
    for f in files:
        print(image_over)
        print("Image_over")
        if ".jpg" or ".JPG" in f:
            print(f)
            image1 = Image.open(positive_files + "/" + f)
            print(image1)
            #root.geometry('%dx%d' % (image1.size[0], image1.size[1]))
            #print(image1.size[0], image1.size[1])
            tkpi = ImageTk.PhotoImage(image1)
            label_image = tk.Label(displaycanvas, image=tkpi)
            label_image.img = tkpi
            if image_over == 500:
                col_num = 0
                print("Image has passed the threshold")
                label_image.grid(row=row_num+1, column = col_num)
                ychange = ychange -15
            label_image.place(x=image_over, y= ychange, width=image1.size[0], height=image1.size[1])

            displaycanvas.create_image(50,10,image=tkpi,anchor=CENTER)

            displaycanvas.bind()
            root.title(f)

            #if old_label_image is not None:
                 #old_label_image.destroy()
            old_label_image = image1
            image_over = image_over + old_label_image.size[0]

 
displaybutton = tk.Button(root, text='Display Detections', command=display_images)
displaybutton.grid(column = entrycol, row = 5, sticky = E)
#displaybutton.pack(side=BOTTOM)
#displayframe.pack(side=BOTTOM)
#imageframe.pack(side=TOP)
#predictframe.pack()


root.mainloop()
root.withdraw()


# split the ui into frames, top frame should be the predict button and variables

# side frame should be where you can see the images that have been predicted on

# then the other side frame should be the partioned image like how they have it in ecocensus

# learn how to switch ui tabs as well
#TODO: Find all the .py files and connectors in the original Ecocensus project
#TODO: By connectors I mean things like