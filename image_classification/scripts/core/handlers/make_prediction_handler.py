import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, CLASSIFIED_IMAGES, CNN_PREDICTION_MODEL
from flask import session

class ClassifyImages:
    def __init__(self, input_dir,input_static_dir=STATIC_FOLDER_IMAGES, output_dir=CLASSIFIED_IMAGES, model_path=CNN_PREDICTION_MODEL, input_split_dimension = None):
        self.input_dir = os.path.join(input_static_dir, input_dir)
        self.output_dir = output_dir
        self.input_split_dimesion = input_split_dimension
        # Consider loading the model only once during initialization
        self.model = load_model(model_path, compile=False)

    def classify_images(self,k,folder_name,combined_folder):
        for j in range(self.input_split_dimesion):
            for i in range(self.input_split_dimesion):
                img_path = os.path.join(self.input_dir, f"{k}_{j}_{i}.png")
                img = cv2.imread(img_path)
                img2 = cv2.resize(img, (120, 120))
                img2 = np.array(img2)
                img2 = np.expand_dims(img2, axis=0)

                prediction = self.model.predict(img2)
                print("prediction", prediction)
                print(img_path)

                # Create a green background for human, red for non-human
                if prediction > 0.2: 
                    background_color = (0, 255, 0)  # Green (BGR format)
                    output_dir = os.path.join(self.output_dir, folder_name)
                else:
                    background_color = (0, 0, 255)  # Red (BGR format)
                    output_dir = os.path.join(self.output_dir, f"non_{folder_name}")

                # # Create a new image with the specified background color
                # new_img = np.full_like(img, background_color)
                # # Combine the original image with the background
                # combined_img = cv2.addWeighted(img, 0.7, new_img, 0.3, 0)

                temp = np.zeros((img.shape[0]+20,img.shape[1]+20,3))
                combined_img = np.full_like(temp, background_color)
                combined_img[10:-10,10:-10,:] = img

                # Save the combined image to the "combined" folder within CLASSIFIED_IMAGES
                combined_output_dir = os.path.join(self.output_dir, combined_folder)
                if not os.path.exists(combined_output_dir):
                    os.makedirs(combined_output_dir)

                combined_output_path = os.path.join(combined_output_dir, f"{k}_{j}_{i}.png")
                cv2.imwrite(combined_output_path, combined_img)

                # Copy the image to the "human" or "non-human" folder
                if prediction > 0.2: 
                    human_output_path = os.path.join(output_dir, f"{k}_{j}_{i}.png")
                else:
                    non_human_output_path = os.path.join(output_dir, f"{k}_{j}_{i}.png")

                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                cv2.imwrite(human_output_path if prediction > 0.2 else non_human_output_path, combined_img)



# class ClassifyImages:
#     def __init__(self, input_dir=STATIC_FOLDER_IMAGES_SPLITIMAGES, output_dir=CLASSIFIED_IMAGES, model_path=CNN_PREDICTION_MODEL, input_split_dimension = None):
#         self.input_dir = input_dir
#         self.output_dir = output_dir
#         self.input_split_dimesion = input_split_dimension
#         # Consider loading the model only once during initialization
#         self.model = load_model(model_path, compile=False)

#     def classify_images(self):
#         for j in range(self.input_split_dimesion):
#             for i in range(self.input_split_dimesion):
#                 img_path = os.path.join(self.input_dir, f"{j}_{i}.png")
#                 img = cv2.imread(img_path)
#                 img2 = cv2.resize(img, (120, 120))
#                 img2 = np.array(img2)
#                 img2 = np.expand_dims(img2, axis=0)

#                 prediction = self.model.predict(img2)
#                 print("prediction", prediction)
#                 print(img_path)

#                 # Create a green background for human, red for non-human
#                 if prediction > 0.2: 
#                     background_color = (0, 255, 0)  # Green (BGR format)
#                     output_dir = os.path.join(self.output_dir, 'human')
#                 else:
#                     background_color = (0, 0, 255)  # Red (BGR format)
#                     output_dir = os.path.join(self.output_dir, 'non_human')

#                 # # Create a new image with the specified background color
#                 # new_img = np.full_like(img, background_color)
#                 # # Combine the original image with the background
#                 # combined_img = cv2.addWeighted(img, 0.7, new_img, 0.3, 0)

#                 temp = np.zeros((img.shape[0]+20,img.shape[1]+20,3))
#                 combined_img = np.full_like(temp, background_color)
#                 combined_img[10:-10,10:-10,:] = img

#                 # Save the combined image to the "combined" folder within CLASSIFIED_IMAGES
#                 combined_output_dir = os.path.join(self.output_dir, 'combined')
#                 if not os.path.exists(combined_output_dir):
#                     os.makedirs(combined_output_dir)

#                 combined_output_path = os.path.join(combined_output_dir, f"{j}_{i}.png")
#                 cv2.imwrite(combined_output_path, combined_img)

#                 # Copy the image to the "human" or "non-human" folder
#                 if prediction > 0.2: 
#                     human_output_path = os.path.join(output_dir, f"{j}_{i}.png")
#                 else:
#                     non_human_output_path = os.path.join(output_dir, f"{j}_{i}.png")

#                 if not os.path.exists(output_dir):
#                     os.makedirs(output_dir)

#                 cv2.imwrite(human_output_path if prediction > 0.2 else non_human_output_path, combined_img)

