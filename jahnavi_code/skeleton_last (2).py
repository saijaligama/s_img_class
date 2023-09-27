import cv2
from skimage import morphology
from skimage.morphology import skeletonize
import numpy as np
from numpy import asarray
import os
from PIL import Image
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/jahna/OneDrive/Documents/GitHub/Project/Image_Filter_Reconstruction/Output Images/File_06.png") # Read image

sharpen_filter = np.array([[0, -1, 0], [-1, 8, -1], [0, -1, 0]])
sharped = cv2.filter2D(img, -1, sharpen_filter)
image_median = cv2.medianBlur(sharped,3)

image_medresol = cv2.pyrDown(img)
image_lowresol = cv2.pyrDown(image_medresol)

Com_resol = cv2.pyrUp(image_medresol) * cv2.pyrUp(cv2.pyrUp(image_lowresol)) * image_median

kernel = np.ones((1,5), np.uint8)
img_erosion = cv2.erode(Com_resol, kernel, iterations=2)
sharped_img = cv2.filter2D(img_erosion, -1, sharpen_filter)
#median = cv2.medianBlur(sharped_img,3)
kernel2 = np.ones((5,1), np.uint8)
img_dilation = cv2.dilate(sharped_img, kernel2, iterations=2)

#erosion = cv2.resize(sharped_img,(500,500))
#Com_resol = cv2.resize(Com_resol,(500,500))
#dilation = cv2.resize(img_dilation,(500,500))

skeleton = skeletonize(img_dilation)

image = cv2.imread("C:/Users/jahna/OneDrive/Documents/GitHub/Project/new_masks/Test/6.png") # Read image

thresh = 128
img_binary = cv2.threshold(skeleton, thresh, 255, cv2.THRESH_BINARY)[1]
output_path = "C:/Users/jahna/OneDrive/Documents/GitHub/Project/Image_Filter_Reconstruction/Skeleton_Images"
img_binary = Image.fromarray(img_binary)

#img_binary.save(os.path.join(output_path, '6.png'))

#sharped_output = cv2.resize(sharped,(500,500))
#cv2.imshow('Feature Map', sharped_output)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

fig, ax = plt.subplots(ncols=4, subplot_kw={'adjustable': 'box'})
# ax = axes.ravel()

ax[0].imshow(image)
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