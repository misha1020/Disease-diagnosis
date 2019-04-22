import numpy as np
import sys
import os
import cv2
from keras.preprocessing import image
from keras.models import load_model
from PIL import Image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if len(sys.argv) == 1:
    print('Нет параметров для запуска!')
    sys.exit(1)

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

def ConverPILtoOpenCV(pil_image):
    numpy_image = np.array(pil_image)  
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image

def main():
    filename = "../Test/" + sys.argv[1]

    '''
    print(filename)
    splited = filename.split(".jpg")
    imageInput = Image.open(filename) 
    #splited = filename.split(".jpg")
    imageInput = Square(imageInput)
    imageInput = ConverPILtoOpenCV(imageInput)
    imageInput = Blur(imageInput)
    imageInput = Binary(imageInput)
    
    os.remove(filename)
    cv2.imwrite(splited[0] + ".jpg", imageInput)
    '''

    img = image.load_img(filename, target_size=(256, 256))

    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)

    loaded_model = load_model('Model_Univ_3.h5')
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    prediction = loaded_model.predict(x)
    classes=['Онкология', 'Не онкология']
    print(classes[np.argmax(prediction)])

main()