#!/user/bin/python3.5
from PIL import Image
import get_lat_lon_exif_pil as gll
import utm
import os, sys
import cv2
import numpy as np
import struct
import scipy
import scipy.misc
import scipy.cluster

def main(directorys):
    rootdir = directorys +'/' #'/Users/bound_to_love/Downloads/Test02142018'
    directory = os.path.dirname(directorys + '/Partitions/') #/Users/bound_to_love/Downloads/Test02142018/Partitions/')
    if os.path.exists(directory):
        print ("Directory already exists")
    if not os.path.exists(directory):
        os.makedirs(str(directory))
        print ("Directory made for partitions")
    f = open(str(directory) + "/Drone_coords.txt", "w+")
    files = os.listdir(rootdir)
    for file in files:
        if ".JPG" or ".jpg" in file:
            image = Image.open(str(rootdir + file))
            exif_data = gll.get_exif_data(image)
            dir, lat, lon = gll.get_lat_lon(exif_data)
            f.write((file + " " + str(dir) + " "+ str(lat) + " " + str(lon) + " " + str(image.size[0]) + " " + str(image.size[1])) + str("\n"))
            imgPartition = cv2.imread(rootdir + file)
            x, y, c = imgPartition.shape
            xp = len(str(x))
            yp = len(str(y))
            i, j = 0, 0
            #while i < (x/10)*10:
                #while j < (y/10)*10:
                    #partition = imgPartition.crop((i, j, (i + x / 10), (j + y / 10)))
            while i < x:
                i2 = i + 300
                while j < y:
                    j2 = j + 300
                    newfile = directory + "/" + str(j).zfill(yp) + "_" + str(i).zfill(xp) + "_" + file
                    partition = imgPartition[i:i2, j:j2]#cv2.resize(imgPartition[i:i2, j:j2],(x, y), interpolation = cv2.INTER_LINEAR)
                    cv2.imwrite(newfile, partition)
                    #j += y / 10
                    j += 300
                #i += x / 10
                i += 300
                j = 0
    f.close()

if __name__ == "__main__":
    main()
