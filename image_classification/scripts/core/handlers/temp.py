import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
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
                    # Create a green background
                    background_color = (0, 255, 0)  # Green (BGR format)
                else:
                    # Create a red background
                    background_color = (0, 0, 255)  # Red (BGR format)

                # Create a new image with the specified background color
                new_img = np.full_like(img, background_color)
                # Combine the original image with the background
                combined_img = cv2.addWeighted(img, 0.7, new_img, 0.3, 0)

                if prediction > 0.2: 
                    output_dir_human = os.path.join(self.output_dir, 'human')
                    if not os.path.exists(output_dir_human):
                        os.mkdir(output_dir_human)
                    cv2.imwrite(os.path.join(output_dir_human, f"{j}_{i}.png"), combined_img)
                else:
                    output_dir_non_human = os.path.join(self.output_dir, 'non_human')
                    if not os.path.exists(output_dir_non_human):
                        os.mkdir(output_dir_non_human)
                    cv2.imwrite(os.path.join(output_dir_non_human, f"{j}_{i}.png"), combined_img)


