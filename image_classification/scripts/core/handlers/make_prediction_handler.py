import cv2
import numpy as np
import os
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


# Import the required constant from your constants module
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES_SPLITIMAGES,CLASSIFIED_IMAGES,CNN_PREDICTION_MODEL

class ClassifyImages:

    def __init__(self, input_dir=STATIC_FOLDER_IMAGES_SPLITIMAGES, output_dir = CLASSIFIED_IMAGES, model_path=CNN_PREDICTION_MODEL):
        self.input_dir = input_dir
        self.output_dir = output_dir
        # Consider loading the model only once during initialization
        self.model = load_model(model_path, compile=False)

    def classify_images(self):
        for j in range(8): 
            for i in range(8):
                img_path = os.path.join(self.input_dir, f"{j}_{i}.png")
                img = cv2.imread(img_path)
                img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img2 = cv2.resize(img2, (120, 120))
                img2 = np.array(img2)
                img2 = np.expand_dims(img2, axis=0)

                prediction = self.model.predict(img2)
                print("prediction", prediction)
                print(img_path)

                if prediction > 0.2: 
                    output_dir_human = os.path.join(self.output_dir, 'Human')
                    if not os.path.exists(output_dir_human):
                        os.mkdir(output_dir_human)
                    cv2.imwrite(os.path.join(output_dir_human, f"{j}_{i}.png"), img)
                else:
                    output_dir_non_human = os.path.join(self.output_dir, 'Non_human')
                    if not os.path.exists(output_dir_non_human):
                        os.mkdir(output_dir_non_human)
                    cv2.imwrite(os.path.join(output_dir_non_human, f"{j}_{i}.png"), img)

# Example Usage
# classifier = ImageClassifier()
# classifier.classify_images()
