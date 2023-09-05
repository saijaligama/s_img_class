# Applying filters
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import model_from_json
from skimage.filters import frangi
from skimage import color
import matplotlib.pyplot as plt
from tf_keras_vis.saliency import Saliency
from tf_keras_vis.utils import normalize
from tf_keras_vis.utils.model_modifiers import ReplaceToLinear
import os
import numpy as np

def score_function(output):
    # Replace 0 with the desired class index you want to visualize
    return output[:, 0]

path = r"C:\Users\saija\Desktop\Sharma\image_classification\static\images\split_images"
proj_dir = r"C:\Users\saija\Desktop\Sharma\image_classification\static\images"

img_files = [os.path.join(path, x) for x in os.listdir(path)]

# Load json and create model
json_file = open('.\image_classification\static\cnn_models\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# Load weights into the model
loaded_model.load_weights(".\image_classification\static\cnn_models\model.h5")
print("Loaded model from disk")

loaded_model.compile(optimizer='adam',
                     loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                     metrics=['accuracy'])

# Visualization 
test_sample_img = img_files[1]
test_img = load_img(test_sample_img)
test_img_array = img_to_array(test_img)
test_img_array = np.expand_dims(test_img_array, axis=0)

# Create Saliency object.
saliency = Saliency(loaded_model,
                    model_modifier=ReplaceToLinear(),
                    clone=False)

# Generate saliency map
#saliency_map = saliency(test_img_array,
 #                       tf.keras.losses.MeanSquaredError(),
  #                      smooth_samples=20)  # Use smooth_samples to make result smoother
  
saliency_map = saliency(score_function, test_img_array)

saliency_map = normalize(saliency_map)

output_path_dir = os.path.join(proj_dir, "Reconstructed_Images")
for img in img_files:
    image = load_img(img)
    img_array = img_to_array(image)
    
    img_array = img_array.astype('float32')
    test_img = img_array / 255.
    
    test_gray = color.rgb2gray(test_img)
    frangi_img = frangi(test_gray, sigmas=range(1, 6, 2), scale_range=None,
                        scale_step=None, alpha=1, beta=1, gamma=150,
                        black_ridges=True, mode='reflect', cval=0)
    
    filter_image = saliency_map[0] * frangi_img
    output_file_path = os.path.join(output_path_dir, os.path.basename(img))
    plt.imsave(output_file_path, filter_image, cmap='binary_r')
