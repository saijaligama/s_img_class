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
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES
from scripts.constants.global_constants import JSON_MODEL, CNN_MODEL, CLASSIFIED_IMAGES
# from constants import base_dir, model_json_path, model_weights_path

class ApplySaliency:

    def __init__(self):
        self.proj_dir = CLASSIFIED_IMAGES
        self.path = os.path.join(self.proj_dir, "human")
        self.img_files = [os.path.join(self.path, x) for x in os.listdir(self.path)]
        
        self.loaded_model = self._load_model(JSON_MODEL, CNN_MODEL)
        self.loaded_model.compile(optimizer='adam',
                                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                                  metrics=['accuracy'])
        print("Loaded model from disk")

    def _load_model(self, json_path, weights_path):
        with open(json_path, 'r') as json_file:
            loaded_model_json = json_file.read()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(weights_path)
        return loaded_model

    @staticmethod
    def score_function(output):
        return output[:, 0]

    def process_images(self):
        saliency = Saliency(self.loaded_model,
                            model_modifier=ReplaceToLinear(),
                            clone=False)
        test_sample_img = self.img_files[1]
        test_img = load_img(test_sample_img)
        test_img_array = img_to_array(test_img)
        test_img_array = np.expand_dims(test_img_array, axis=0)
        
        saliency_map = saliency(self.score_function, test_img_array)
        saliency_map = normalize(saliency_map)

        output_path_dir = os.path.join(STATIC_FOLDER_IMAGES, "saliency_images")
        for img in self.img_files:
            self._save_processed_image(img, saliency_map, output_path_dir)

    def _save_processed_image(self, img, saliency_map, output_dir):
        image = load_img(img)
        img_array = img_to_array(image)
        img_array = img_array.astype('float32')
        test_img = img_array / 255.
        
        test_gray = color.rgb2gray(test_img)
        frangi_img = frangi(test_gray, sigmas=range(1, 6, 2), scale_range=None,
                            scale_step=None, alpha=1, beta=1, gamma=150,
                            black_ridges=True, mode='reflect', cval=0)
        
        filter_image = saliency_map[0] * frangi_img
        output_file_path = os.path.join(output_dir, os.path.basename(img))
        plt.imsave(output_file_path, filter_image, cmap='binary_r')
