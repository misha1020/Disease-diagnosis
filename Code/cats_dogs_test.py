from keras.utils import np_utils
from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Загружаем изображение
img_path = '6.jpg'
img = image.load_img(img_path, target_size=(150, 150)) #, grayscale=True

# Преобразуем изображением в массив numpy
x = image.img_to_array(img)

# Инвертируем и нормализуем изображение
#x = 255 - x
x /= 255
x = np.expand_dims(x, axis=0)

json_file = open("cats_dogs.json", "r")
loaded_model_json = json_file.read()
json_file.close()
# Создаем модель на основе загруженных данных
loaded_model = model_from_json(loaded_model_json)
# Загружаем веса в модель
loaded_model.load_weights("cats_dogs.h5")

loaded_model.compile(loss="binary_crossentropy", optimizer='adam', metrics=["accuracy"])

prediction = loaded_model.predict(x)
classes=['кот', 'собака']
print(classes[np.argmax(prediction)])
