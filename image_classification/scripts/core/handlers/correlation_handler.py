import numpy as np
from scipy.stats import pearsonr
import os
import cv2
import matplotlib.pyplot as plt
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES

class CorrelationProcessor:
    def __init__(self):
        self.static_folder_images = STATIC_FOLDER_IMAGES
        self.img_dir = r"image_classification/static/images/skeleton_images"
        self.img_ori = r"test_images/human_non_human/"
        self.corr_folder = r"image_classification/static/images/correlation_images"
        self.uploaded_folder = r"image_classification/static/images/uploaded_images"
        self.images = []
        self.img_names = []

    def check_folder(self,dir_path=None, subfolder_names=None):
        if dir_path == None:
            dir_path = self.static_folder_images
            subfolder_names = ['correlation_images'] 
        else:
            dir_path = os.path.join(self.static_folder_images, 'classified_images')
            subfolder_names = ['human','non_human','combined']

        for subfolder_name in subfolder_names:
            subfolder_path = os.path.join(dir_path,subfolder_name)

            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)  # Create the subfolder if it doesn't exist
            else:
                for f in os.listdir(subfolder_path):
                    item_path = os.path.join(subfolder_path, f)
                    if os.path.isfile(item_path):
                        os.remove(item_path) 
                    else:
                        self.check_folder(dir_path)

    def process_correlation(self,image_name,corr_coef):
        self.check_folder()
        img_name = ""
        for filename in os.listdir(self.img_dir):
            # print(filename)
            # print("image_name",image_name)
            img = cv2.imread(os.path.join(self.img_dir, filename))
            img_dsam = cv2.pyrDown(img)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_data = np.array(img_dsam, dtype=np.float64) / 255
            self.img_names.append(filename)
            if image_name + ".png" == filename:
                img_name = img_data
            self.images.append(img_data)

        correlation_coefficients = []
        max_corr = -1.0
        max_img_name = ""
        for i in range(len(self.images)):
            # corr, _ = pearsonr(self.images[0].flatten(), self.images[i].flatten())
            # correlation_coefficients.append((corr, self.images[0], self.images[i]))

            corr, _ = pearsonr(img_name.flatten(), self.images[i].flatten())
            if corr >0.99:
                continue
            else:
                # max_corr = corr
                # max_img_name = self.images[i]
                # print("inside loop",max_corr)
                if corr > max_corr:
                    max_corr = corr
                    max_img_name = self.images[i]
        correlation_coefficients.append((max_corr, img_name, max_img_name))
        # print(max_corr)

        # print(correlation_coefficients)

        for corr, img1, img2 in correlation_coefficients:
            # print(type(corr))
            # print(type(corr_coef))
            corr_coef = float(corr_coef)
            # print(type(corr_coef))
            # if corr >= corr_coef:
            img1_idx = np.where(np.all(self.images == img1, axis=(1, 2, 3)))[0][0]
            img2_idx = np.where(np.all(self.images == img2, axis=(1, 2, 3)))[0][0]
            img1_name = self.img_names[img1_idx]
            img2_name = self.img_names[img2_idx]

            img1_blur = cv2.GaussianBlur(cv2.imread(os.path.join(self.img_dir, img1_name)), (5, 5), 5)
            img2_blur = cv2.GaussianBlur(cv2.imread(os.path.join(self.img_dir, img2_name)), (5, 5), 5)

            plt.figure()
            plt.subplot(231)
            plt.imshow(cv2.imread(os.path.join(self.img_ori, img1_name)))
            plt.title("Image")
            plt.axis("off")
            plt.subplot(232)
            plt.imshow(cv2.imread(os.path.join(self.img_ori, img2_name)))
            plt.title("Image")
            plt.axis("off")
            # plt.imshow(cv2.imread(os.path.join(self.img_dir, img1_name)))
            # plt.title("Dilation")
            # plt.axis("off")
            # plt.subplot(233)
            # plt.imshow(cv2.imread(os.path.join(self.img_ori, img2_name)))
            # plt.title("Image")
            # plt.axis("off")
            # plt.subplot(234)
            # plt.imshow(cv2.imread(os.path.join(self.img_dir, img2_name)))
            # plt.title("Dilation")
            # plt.axis("off")
            plt.suptitle("Correlation Coefficient: {:.2f}".format(corr))
            plt.savefig(os.path.join(self.corr_folder, "{}_{}_corr.png".format(img1_name, img2_name)))
                #plt.show()

    def process_correlation_2(self,image_0,image_1):
        self.check_folder()
        img_name_0 = ""
        img_name_1 = ""
        for filename in os.listdir(self.img_dir):
            print(filename)
            # print("image_name",image_name)
            img = cv2.imread(os.path.join(self.img_dir, filename))
            img_dsam = cv2.pyrDown(img)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_dsam = cv2.pyrDown(img_dsam)
            img_data = np.array(img_dsam, dtype=np.float64) / 255
            self.img_names.append(filename)
            if image_0 + ".png" == filename :
                img_name_0 = img_data
            elif image_1 + ".png" == filename:
                img_name_1 = img_data
            self.images.append(img_data)

        correlation_coefficients = []
        corr, _ = pearsonr(img_name_0.flatten(), img_name_1.flatten())
        correlation_coefficients.append((corr, img_name_0, img_name_1))

        # print(correlation_coefficients)

        for corr, img1, img2 in correlation_coefficients:
            # corr_coef = float(corr_coef)
            # print(type(corr_coef))
            # if corr >= corr_coef:
            img1_idx = np.where(np.all(self.images == img1, axis=(1, 2, 3)))[0][0]
            img2_idx = np.where(np.all(self.images == img2, axis=(1, 2, 3)))[0][0]
            img1_name = self.img_names[img1_idx]
            img2_name = self.img_names[img2_idx]

            img1_blur = cv2.GaussianBlur(cv2.imread(os.path.join(self.img_dir, img1_name)), (5, 5), 5)
            img2_blur = cv2.GaussianBlur(cv2.imread(os.path.join(self.img_dir, img2_name)), (5, 5), 5)

            plt.figure()
            plt.subplot(231)
            plt.imshow(cv2.imread(os.path.join(self.uploaded_folder, img1_name)))
            plt.title("{}".format(img1_name))
            plt.axis("off")
            plt.subplot(232)
            plt.imshow(cv2.imread(os.path.join(self.uploaded_folder, img2_name)))
            plt.title("{}".format(img2_name))
            plt.axis("off")
            # plt.imshow(cv2.imread(os.path.join(self.img_dir, img1_name)))
            # plt.title("Dilation")
            # plt.axis("off")
            # plt.subplot(233)
            # plt.imshow(cv2.imread(os.path.join(self.img_ori, img2_name)))
            # plt.title("Image")
            # plt.axis("off")
            # plt.subplot(234)
            # plt.imshow(cv2.imread(os.path.join(self.img_dir, img2_name)))
            # plt.title("Dilation")
            # plt.axis("off")
            plt.suptitle("Correlation Coefficient: {:.2f}".format(corr))
            plt.savefig(os.path.join(self.corr_folder, "{}_{}_corr.png".format(img1_name, img2_name)))
            

