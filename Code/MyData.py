import numpy as np
import sys
import os
import cv2
from keras.preprocessing import image
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if len(sys.argv) == 1:
    print('Нет параметров для запуска!')
    sys.exit(1)

def Blur(img):
    blurGaus = cv2.GaussianBlur(img, (5, 5), 0) 
    return blurGaus

def Binary(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retGl, thGlobal = cv2.threshold(imgGray, 165, 255, cv2.THRESH_BINARY)
    return thGlobal

def ConverPILtoOpenCV(pil_image):
    numpy_image = np.array(pil_image)  
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
    return opencv_image

img_path = "../Test/" + sys.argv[1]
img = image.load_img(img_path, target_size=(800, 800))
#img = ConverPILtoOpenCV(img)
#img = Blur(img)
#img = Binary(img)

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

loaded_model = load_model('MyData_Model_Bin25x800x45x5x3.h5')
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

prediction = loaded_model.predict(x)
classes=['Онкология', 'Не онкология']
print(classes[np.argmax(prediction)])