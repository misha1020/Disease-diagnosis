import shutil
import os
import numpy as np 
from PIL import Image
import cv2

data_dir = "../All Images Mixed"
train_dir = "../Images 299/train"
val_dir = "../Images 299/val"
val_data_portion = 0.2

nb_images = 35

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "Onco"))
    os.makedirs(os.path.join(dir_name, "NotOnco"))

create_directory(train_dir)
create_directory(val_dir)

def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index):
        shutil.copy(os.path.join(source_dir, "Onco_" + str(i) + ".jpg"),
                    os.path.join(dest_dir, "Onco"))
        shutil.copy(os.path.join(source_dir, "NotOnco_" + str(i) + ".jpg"), 
                   os.path.join(dest_dir, "NotOnco"))

start_val_data_idx = int(nb_images * (1 - val_data_portion))

print(start_val_data_idx)
print("Изображений скопировано в train directory.")

copy_images(0, start_val_data_idx, data_dir, train_dir)
copy_images(start_val_data_idx, nb_images, data_dir, val_dir)