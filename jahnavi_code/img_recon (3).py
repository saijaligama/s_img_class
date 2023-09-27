import os
import warnings
warnings.filterwarnings("ignore")

# Fetching data    
path = r"C:\Users\jahna\OneDrive\Documents\GitHub\Project\new_masks\Test\test_cropped_8x8\human"
proj_dir = r"C:\Users\jahna\OneDrive\Documents\GitHub\Project\Image_Filter_Reconstruction"

img_files  = [os.path.join(path, x) for x in os.listdir(path)]

# Applying filters
import keras
from keras.preprocessing.image import img_to_array, load_img
from keras.models import model_from_json
import tensorflow as tf
from skimage.filters import frangi
from skimage import color
from vis.utils import utils
import matplotlib.pyplot as plt
from vis.visualization import visualize_saliency


# load json
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


# Loading model for visualization varaible
layer_index = utils.find_layer_idx(loaded_model, 'saliency')
test_sample_img = img_files[1]
test_img= load_img(test_sample_img )
test_img_array = img_to_array(test_img)
visualization = visualize_saliency(loaded_model, layer_index, filter_indices=None, 
                                   seed_input=test_img_array , backprop_modifier=None)


# cmap_val = 'binary_r'
output_path_dir = os.path.join(proj_dir, "Reconstructed_Images")
for img in img_files:
    # print("The image file is",img)
    image = load_img(img)
    img_array = img_to_array(image)
    
    img_array = img_array .astype('float32')
    test_img = img_array / 255.
    
    test_gray = color.rgb2gray(test_img)
    frangi_img = frangi(test_gray, sigmas=range(1, 6, 2), scale_range=None,
               scale_step=None, alpha=1, beta=1, gamma=150,
               black_ridges=True, mode='reflect', cval=0)
    
    filter_image = visualization * frangi_img
    output_file_path = os.path.join(output_path_dir, os.path.basename(img))
    plt.imsave(output_file_path, filter_image, cmap = 'binary_r')