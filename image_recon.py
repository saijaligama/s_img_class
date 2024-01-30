import numpy as np
from scipy.stats import pearsonr
import os
import cv2
import matplotlib.pyplot as plt

# specify the directory containing the images
img_dir = r"image_classification/static/images/skeleton_images"
img_ori = r"test_images/human_non_human/"
corr_folder = r"image_classification/static/images/correlation_images"
#feature_map = r"C:\Users\jahna\OneDrive\Documents\GitHub\Project\Image_Filter_Reconstruction\Combined resolution"



# create a list to store the images and their names
images = []
img_names = []

corr_coef = 0.2

# iterate through the images in the directory
for filename in os.listdir(img_dir):
    # read the image
    img = cv2.imread(os.path.join(img_dir, filename))
    #blur = cv2.GaussianBlur(img, (5, 5), 5)
    #img_dsam = cv2.pyrDown(blur)
    img_dsam = cv2.pyrDown(img)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    # convert image to a 2D array of pixels
    img_data = np.array(img_dsam, dtype=np.float64) / 255
    img_names.append(filename)
    # add the image to the list
    images.append(img_data)

# calculate the correlation coefficient for each pair of images
#correlation_coefficients = []
#for i in range(len(images)):
 #   for j in range(i+1, len(images)):
  #      corr, _ = pearsonr(images[i].flatten(), images[j].flatten())
   #     correlation_coefficients.append((corr, images[i], images[j]))
        
# calculate the correlation coefficient for each pair of images
correlation_coefficients = []
for i in range(len(images)):
    corr, _ = pearsonr(images[0].flatten(), images[i].flatten())
    correlation_coefficients.append((corr, images[0], images[i]))

# display the correlation coefficients and the images
for corr, img1, img2 in correlation_coefficients:
    if corr >= corr_coef: 
        # extract image names from the full paths
        img1_idx = np.where(np.all(images == img1, axis=(1, 2, 3)))[0][0]
        img2_idx = np.where(np.all(images == img2, axis=(1, 2, 3)))[0][0]
        img1_name = img_names[img1_idx]
        img2_name = img_names[img2_idx]

        # apply Gaussian blur to the original images
        img1_blur = cv2.GaussianBlur(cv2.imread(os.path.join(img_dir, img1_name)), (5, 5), 5)
        img2_blur = cv2.GaussianBlur(cv2.imread(os.path.join(img_dir, img2_name)), (5, 5), 5)



        plt.figure()
        plt.subplot(231)
        plt.imshow(cv2.imread(os.path.join(img_ori, img1_name)))
        plt.title("Image")
        plt.axis("off")
        #plt.subplot(232)
        #plt.imshow(cv2.imread(os.path.join(feature_map, img1_name)))
        #plt.title("Feature map")
        #plt.axis("off")
        plt.subplot(232)
        plt.imshow(cv2.imread(os.path.join(img_dir, img1_name)))
        plt.title("Dilation")
        plt.axis("off")
        plt.subplot(233)
        plt.imshow(cv2.imread(os.path.join(img_ori, img2_name)))
        plt.title("Image")
        plt.axis("off")
        #plt.subplot(235)
        #plt.imshow(cv2.imread(os.path.join(feature_map, img2_name)))
        #plt.title("Feature Map")
        #plt.axis("off")
        plt.subplot(234)
        plt.imshow(cv2.imread(os.path.join(img_dir, img2_name)))
        plt.title("Dilation")
        plt.axis("off")
        plt.suptitle("Correlation Coefficient: {:.2f}".format(corr))
        plt.savefig("{}/{}_{}_corr.png".format(corr_folder,img1_name,img2_name))
        #plt.show()
