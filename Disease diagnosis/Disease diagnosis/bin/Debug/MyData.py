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

#if len(sys.argv) == 1:
#    print('Нет параметров для запуска!')
#    sys.exit(1)

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
    modelName = str(sys.argv[1])
    loaded_model = load_model(modelName)
    filename = str(sys.argv[2])
    #filename = "C:\\Users\\shenmay\\Documents\\GitHub\\Kurs\\All Images\\NotOnco_15.JPG"
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
    classes=['No', 'Yes']
    print(classes[round(float(prediction[[0]]))])
    
main()