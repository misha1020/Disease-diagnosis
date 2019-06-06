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
    imgNames = filter(lambda x: x.endswith(".jpg") or x.endswith(".JPG") or x.endswith(".JPEG"), files)
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
    direc = "../All Images Mixed/"
    
    imgs = LoadFilesNamesFromDir(direc)
    count = 0
    for Image in imgs:
        splited = Image.split("_")
        if (splited[0] == "NotOnco"):
            currentClass = "NotOnco_"
        elif (splited[0] == "Onco"):
            currentClass = "Onco_"
        if (count%3 == 2):
            os.rename(direc + Image, direc + currentClass +"2_" + str(count) + ".JPG")
        elif (count%3 == 1):
            os.rename(direc + Image, direc + currentClass + "1_" + str(count) + ".JPG")
        else:
            os.rename(direc + Image, direc + currentClass + "0_" + str(count) + ".JPG")
        count += 1
    
    imgs = LoadFilesNamesFromDir(direc)
    # Количество элементов данных в одном классе
    nb_images = 35
    i = 0
    for Image in imgs:
        currentName = Image.split("_")
        os.rename(direc + Image, direc + currentName[0] + "_" + str(i%nb_images) + ".JPG")
        i += 1

#Sort()
Rename()
