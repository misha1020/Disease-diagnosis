import numpy
import os
from keras.preprocessing import image
from keras.models import load_model
from keras.datasets import mnist
from keras.utils import np_utils

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
img_rows, img_cols = 28, 28

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
X_test = X_test.astype('float32')
X_test /= 255
Y_test = np_utils.to_categorical(y_test, 10)    

loaded_model = load_model('model_Nums.h5')
loaded_model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])

scores = loaded_model.evaluate(X_test, Y_test, verbose = 0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100))