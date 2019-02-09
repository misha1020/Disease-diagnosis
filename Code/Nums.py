import numpy
import os
from keras.preprocessing import image
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

img_path = '6.png'
img = image.load_img(img_path, target_size = (28,28), grayscale = True)

x = image.img_to_array(img)

x = 255 - x
x /= 255
x = numpy.expand_dims(x, axis = 0)

loaded_model = load_model('model_Nums.h5')

loaded_model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
prediction = loaded_model.predict(x)
print(numpy.argmax(prediction))