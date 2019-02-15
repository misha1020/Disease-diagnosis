import numpy
import os
import json
import time
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
numpy.random.seed(42)

img_rows, img_cols = 28, 28

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()
model.add(Conv2D(75, kernel_size = (5,5),
                    activation = 'relu',
                    input_shape = input_shape))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.2))
model.add(Conv2D(100, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
#print(model.summary())

model.fit(X_train, Y_train, batch_size = 200, epochs = 10, validation_split = 0.2, verbose = 2)
model.save('model_Nums.h5')

scores = model.evaluate(X_test, Y_test, verbose = 0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100))