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

direc = "../MakeNotOnco/"
imgs = LoadFilesNamesFromDir(direc)
i = 0
for Image in imgs:
    #os.rename(direc + Image, direc + "Onco_" + str(i) + ".JPG")
    os.rename(direc + Image, direc + 'NotOnco_' + str(i) + ".JPG")
    i += 1