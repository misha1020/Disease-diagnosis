import shutil
import os
import numpy as np 
from PIL import Image
import cv2

# Каталог с набором данных
data_dir = "../Less Bin"
# Каталог с данными для обучения
train_dir = "../Images/train"
# Каталог с данными для проверки
val_dir = "../Images/val"
# Каталог с данными для тестирования
test_dir = "../Images/test"
# Часть набора данных для тестирования
test_data_portion = 0.25
# Часть набора данных для проверки
val_data_portion = 0.25
# Количество элементов данных в одном классе
nb_images = 68

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "Onco"))
    os.makedirs(os.path.join(dir_name, "NotOnco"))

create_directory(train_dir)
create_directory(val_dir)
create_directory(test_dir)

def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index):
        shutil.copy(os.path.join(source_dir, "Onco_" + str(i) + ".jpg"),
                    os.path.join(dest_dir, "Onco"))
        shutil.copy(os.path.join(source_dir, "NotOnco_" + str(i) + ".jpg"), 
                   os.path.join(dest_dir, "NotOnco"))

#start_val_data_idx = int(nb_images * (1 - val_data_portion - test_data_portion))
start_val_data_idx = 50
#start_test_data_idx = int(nb_images * (1 - test_data_portion))
start_test_data_idx = 59

print(start_val_data_idx)
print(start_test_data_idx)

copy_images(0, start_val_data_idx, data_dir, train_dir)
copy_images(start_val_data_idx, start_test_data_idx, data_dir, val_dir)
copy_images(start_test_data_idx, nb_images, data_dir, test_dir)