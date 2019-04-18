import os
import string

def Capitalize(myStr):
    return myStr.upper()

def LoadFilesNamesFromDir(dir):
    files = os.listdir(dir)
    for i, file in enumerate(files):
        splited = file.split(".")
        splited[1] = Capitalize(splited[1])
        file = splited[0] + "." + splited[1]
        files[i] = file
    imgNames = filter(lambda x: x.endswith(".PNG") or x.endswith(".BMP") or x.endswith(".JPG") or x.endswith(".JPEG"), files)
    return imgNames

def Rename(): 
    direc = "../Make Not Onco/"
    imgs = LoadFilesNamesFromDir(direc)

    if (direc == "../Make Onco/"):
        currentClass = "Onco_"
    elif (direc == "../Make Not Onco/"):
        currentClass = "NotOnco_"
    else:
        currentClass = "NoInfo_"

    processName = "Process"
    i = 0
    for Image in imgs:
        os.rename(direc + Image, direc + processName + str(i) + ".JPG")
        i += 1

    imgs = LoadFilesNamesFromDir(direc)
    i = 0
    for Image in imgs:
        os.rename(direc + Image, direc + currentClass + str(i) + ".JPG")
        i += 1

def Sort():
    direc = "../All Images/"
    i = 0
    imgs = LoadFilesNamesFromDir(direc)

    for Image in imgs:
        splited = Image.split("_")
        if (splited[0] == "NotOnco"):
            currentClass = "NotOnco__"
        elif (splited[0] == "Onco"):
            currentClass = "Onco__"
        if (i%3 == 2):
            os.rename(direc + Image, direc + currentClass +"2_" + str(i) + ".JPG")
        elif (i%3 == 1):
            os.rename(direc + Image, direc + currentClass + "1_" + str(i) + ".JPG")
        else:
            os.rename(direc + Image, direc + currentClass + "0_" + str(i) + ".JPG")
        i += 1

#Sort()
Rename()
