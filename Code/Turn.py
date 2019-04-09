import os
import cv2
import glob
import numpy as np 
from PIL import Image

def Blur(img):
    blurGaus = cv2.GaussianBlur(img, (5, 5), 0) 
    return blurGaus

def Binary(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retGl, thGlobal = cv2.threshold(imgGray, 165, 255, cv2.THRESH_BINARY)
    return thGlobal

def Turn(img, val):
    (h, w) = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, val, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), borderValue=(255,255,255))
    return rotated

def Square(im, min_size = 256, fill_color = (255, 255, 255)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, ((size - x) // 2, (size - y) // 2))
    return new_im

def Squeeze(img, size):
    wpercent = (size/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((size,hsize), Image.ANTIALIAS)
    return img

def ConverPILtoOpenCV(pil_image):
    numpy_image = np.array(pil_image)  
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image

def main():
    directory = "../Images"
    for dir in ([x[0] for x in os.walk(directory)]):
        for filename in glob.glob(dir + "/*.jpg"):
            print(filename)
            imageInput = Image.open(filename) 
            splited = filename.split(".jpg")
            k = 0
            while (k < 360):
                image = imageInput.copy()           
                image = Square(image)
                image = Squeeze(image, 800)
                image = ConverPILtoOpenCV(image)
                image = Turn(image, k)
                image = Blur(image)
                image = Binary(image)
                cv2.imwrite(splited[0] + "_" + str(k) + ".jpg", image)
                k += 45
            os.remove(filename)

main()
           