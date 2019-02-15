import numpy as np
import sys
import os
from keras.preprocessing import image
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if len(sys.argv) == 1:
    print('Нет параметров для запуска!')
    sys.exit(1)

img_path = "../Converted Images/w8/" + sys.argv[1]
img = image.load_img(img_path, target_size=(150, 150))

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

loaded_model = load_model('model_MyData.h5')
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

prediction = loaded_model.predict(x)
classes=['Онкология', 'Не онкология']
print(classes[np.argmax(prediction)])