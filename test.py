from genericpath import exists
# import streamlit as st
#import cv2
import numpy as np
from math import ceil
#import tensorflow as tf
import os, shutil
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from keras.models import load_model, model_from_json
#from keras.preprocessing.image import img_to_array, load_img
from skimage.filters import frangi
from skimage import color
from vis.utils import utils
import matplotlib.pyplot as plt
from vis.visualization import visualize_saliency


# load json
json_file = open('.\image_classification\static\cnn_models\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights(".\image_classification\static\cnn_models\cnn.h5")
print("Loaded model from disk")
 