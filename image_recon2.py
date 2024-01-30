import numpy as np
from scipy.stats import pearsonr
import os
import cv2

# specify the directory containing the images
img_dir = r"image_classification/static/images/skeleton_images"
img_ori = r"test_images/human_non_human/"
corr_folder = r"image_classification/static/images/correlation_images"

# Choose a reference image (you can change the index as needed)
reference_image_index = 1

# Read the reference image
reference_image = cv2.imread(os.path.join(img_dir,"{}.png".format(reference_image_index)))

# Create a list to store the images and their names
images = []
img_names = []

# Iterate through the images in the directory
for filename in os.listdir(img_dir):
    img = cv2.imread(os.path.join(img_dir, filename))
    img_dsam = cv2.pyrDown(img)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_dsam = cv2.pyrDown(img_dsam)
    img_data = np.array(img_dsam, dtype=np.float64) / 255
    img_names.append(filename)
    images.append(img_data)

# Calculate the correlation coefficient between the reference image and all other images
correlation_coefficients = []
for i in range(len(images)):
    if i == reference_image_index:
        continue  # Skip comparing the reference image with itself
    corr, _ = pearsonr(reference_image.flatten(), images[i].flatten())
    correlation_coefficients.append((corr, reference_image, images[i], img_names[reference_image_index], img_names[i]))

# Display the correlation coefficients and the reference image
for corr, img1, img2, img1_name, img2_name in correlation_coefficients:
    # Apply Gaussian blur to the original images
    img1_blur = cv2.GaussianBlur(cv2.imread(os.path.join(img_dir, img1_name)), (5, 5), 5)
    img2_blur = cv2.GaussianBlur(cv2.imread(os.path.join(img_dir, img2_name)), (5, 5), 5)

    # Display the reference image and the compared image
    plt.figure()
    plt.subplot(231)
    plt.imshow(reference_image)
    plt.title("Reference Image")
    plt.axis("off")
    plt.subplot(232)
    plt.imshow(cv2.imread(os.path.join(img_dir, img2_name)))
    plt.title("Compared Image") 
    plt.axis("off")
    plt.suptitle("Correlation Coefficient: {:.2f}".format(corr))
    plt.savefig("{}/1_2_corr.png".format(corr_folder))
    #plt.savefig(os.path.join(corr_folder,"{}_{}_corr.png".format([reference_image_index],img2_name)))
    #plt.show()
