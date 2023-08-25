from PIL import Image
import base64
from genericpath import exists
from math import ceil
import shutil
import os
import cv2
import numpy as np
from scripts.constants.global_constants import STATIC_FOLDER

# c:\Users\saija\Desktop\imgclass\portal\./img_static



def check_folder():
    folder_name = os.path.join(STATIC_FOLDER_IMAGES, 'split_images')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        for f in os.listdir(folder_name):
            item_path = os.path.join(folder_name, f)
            os.remove(item_path)


def split_images(img: np.ndarray, x_break: int, y_break: int,k : str):
    print("inside split_images")
    print(STATIC_FOLDER)

    height, width, depth = img.shape
    s_height = ceil(height / y_break)
    s_width = ceil(width / x_break)
    
    output_dir = os.path.join(STATIC_FOLDER, 'images')
    output_dir = os.path.join(output_dir, 'split_images')
    if exists(output_dir): shutil.rmtree(output_dir)
    if not exists(output_dir) : os.mkdir(output_dir)

    for i in range(y_break):
        for j in range(x_break):
            temp = img[i * s_height:(i + 1) * s_height, j * s_width:(j + 1) * s_width]
            
            #white_pix = len(np.where(temp == 255)[0])
            cv2.imwrite("{}/{}_{}.png".format(output_dir, i, j), temp)
             
    return output_dir