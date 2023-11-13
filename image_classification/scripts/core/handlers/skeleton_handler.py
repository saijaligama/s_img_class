import cv2
from skimage import morphology
from skimage.morphology import skeletonize
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES
from flask import session

class SkeletonProcessor:
    def __init__(self,reconstructed_path,skeleton_temp):
        self.image_path = os.path.join(STATIC_FOLDER_IMAGES,reconstructed_path,'File_reconstructed_image.png')
        self.output_path = os.path.join(STATIC_FOLDER_IMAGES,'skeleton_images')
        self.skeleton_temp_folder = os.path.join(STATIC_FOLDER_IMAGES,skeleton_temp)

    def process_image(self,image_name):
        skeleton_name = image_name
        img = cv2.imread(self.image_path)

        sharpen_filter = np.array([[0, -1, 0], [-1, 8, -1], [0, -1, 0]])
        sharped = cv2.filter2D(img, -1, sharpen_filter)
        image_median = cv2.medianBlur(sharped, 3)

        image_medresol = cv2.pyrDown(img)
        image_lowresol = cv2.pyrDown(image_medresol)

        Com_resol = cv2.pyrUp(image_medresol) * cv2.pyrUp(cv2.pyrUp(image_lowresol)) * image_median

        kernel = np.ones((1, 5), np.uint8)
        img_erosion = cv2.erode(Com_resol, kernel, iterations=2)
        sharped_img = cv2.filter2D(img_erosion, -1, sharpen_filter)

        kernel2 = np.ones((5, 1), np.uint8)
        img_dilation = cv2.dilate(sharped_img, kernel2, iterations=2)

        skeleton = skeletonize(img_dilation)

        thresh = 128
        img_binary = cv2.threshold(skeleton, thresh, 255, cv2.THRESH_BINARY)[1]

        img_binary = Image.fromarray(img_binary)
        img_binary.save(os.path.join(self.skeleton_temp_folder, '{}.png'.format(skeleton_name)))
        img_binary.save(os.path.join(self.output_path, '{}.png'.format(skeleton_name)))

    def plot_images(self):
        img = cv2.imread(self.image_path)
        sharpen_filter = np.array([[0, -1, 0], [-1, 8, -1], [0, -1, 0]])
        sharped = cv2.filter2D(img, -1, sharpen_filter)
        image_median = cv2.medianBlur(sharped, 3)
        image_medresol = cv2.pyrDown(img)
        image_lowresol = cv2.pyrDown(image_medresol)
        Com_resol = cv2.pyrUp(image_medresol) * cv2.pyrUp(cv2.pyrUp(image_lowresol)) * image_median
        skeleton = skeletonize(cv2.dilate(cv2.filter2D(cv2.erode(Com_resol, np.ones((1, 5), np.uint8), iterations=2), -1, sharpen_filter), np.ones((5, 1), np.uint8), iterations=2))

        fig, ax = plt.subplots(ncols=4, subplot_kw={'adjustable': 'box'})
        ax[0].imshow(img)
        ax[0].axis('off')
        ax[0].set_title('Original Image', fontsize=16)
        ax[1].imshow(sharped)
        ax[1].axis('off')
        ax[1].set_title('Feature Map', fontsize=16)
        ax[2].imshow(Com_resol, cmap='gray')
        ax[2].axis('off')
        ax[2].set_title('Combined Resolution', fontsize=16)
        ax[3].imshow(skeleton, cmap='gray')
        ax[3].axis('off')
        ax[3].set_title('Skeleton', fontsize=16)
        fig.tight_layout()
        plt.show()


