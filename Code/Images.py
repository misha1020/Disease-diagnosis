import numpy as np
import os
from keras.preprocessing import image
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

img_path = 'plane.jpg'
img = image.load_img(img_path, target_size=(32, 32))

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

loaded_model = load_model('model_Images.h5')
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

prediction = loaded_model.predict(x)
classes=['Самолет', 'Автомобиль', 'Птица', 'Кот', 'Олень', 'Собака', 'Лягушка', 'Лошадь', 'Корабль', 'Грузовик']
print(classes[np.argmax(prediction)])