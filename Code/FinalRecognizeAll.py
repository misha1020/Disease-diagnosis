import numpy as np
import sys
import os
import cv2
from keras.preprocessing import image
from keras.models import load_model
from PIL import Image
from keras.models import model_from_json
from keras import optimizers

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def Blur(img):
    blurBilFiltr = cv2.bilateralFilter(img, 9, 75, 75)
    return blurBilFiltr

def Binary(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retGl, thGlobal = cv2.threshold(imgGray, 175, 250, cv2.THRESH_BINARY)
    return thGlobal

def Square(im, min_size = 128, fill_color = (255, 255, 255)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, ((size - x) // 2, (size - y) // 2))
    return new_im

def Squeeze(img, size):
    original_image = img
    max_size = (size, size)
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    return img

def ConvertPILtoOpenCV(pil_image):
    numpy_image = np.array(pil_image)  
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image

def main():
    dirname = '../All Images Final/' # (58x2)
    modelName = 'NewModelTest.h5'
    loaded_model = load_model(modelName)
    k = 0
    while (k < 35):
        filename = dirname + 'NotOnco_' + str(k) + '.jpg' 
        print(filename)
        k += 1

        splited = filename.split(".jpg")
        imageInput = Image.open(filename)
        imageInput = Square(imageInput)
        imageInput = ConvertPILtoOpenCV(imageInput)
        imageInput = Blur(imageInput)
        imageInput = Binary(imageInput)

        filename = splited[0] + "Bin.jpg"
        cv2.imwrite(filename, imageInput)

        img = image.load_img(filename, target_size=(128, 128))

        x = image.img_to_array(img)
        x /= 255
        x = np.expand_dims(x, axis=0)
    
        prediction = loaded_model.predict(x)
        os.remove(filename)
        print(prediction)
        classes=['Не онкология', 'Онкология']
        print(classes[round(float(prediction[[0]]))])
    
main()