from PIL import Image
import base64
from math import ceil
import shutil
import os
import cv2
import numpy as np
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, set_global, global_dimension
import io
from flask import session

class ImageProcessor:

    def __init__(self, static_folder_images=STATIC_FOLDER_IMAGES):
        self.static_folder_images = static_folder_images

    # def check_folder(self):
    #     folder_names
    #     folder_name = os.path.join(self.static_folder_images, 'split_images')
    #     print(os.getcwd())
    #     print(folder_name)
    #     if not os.path.exists(folder_name):
    #         os.makedirs(folder_name)
    #     else:
    #         for f in os.listdir(folder_name):
    #             item_path = os.path.join(folder_name, f)
    #             os.remove(item_path)

    def save_image(image):
        print("inside images")
        base64_decoded = base64.b64decode(image["image"])
        img = Image.open(io.BytesIO(base64_decoded))
        out_path = os.path.join(STATIC_FOLDER_IMAGES,'uploaded_images')
        img.save("{}/{}.{}".format(out_path,image['image_name'],'png'))

    def check_folder(self,dir_path=None, subfolder_names=None):
        if dir_path == None:
            dir_path = self.static_folder_images
            subfolder_names = ['split_images', 'Reconstructed_Images',
                            'saliency_images','classified_images',
                            'skeleton_temp','correlation_images',
                            'split_images_2','saliency_images_2',
                            'Reconstructed_Images_2','skeleton_temp_2',
                            'uploaded_images'] 
        else:
            dir_path = os.path.join(self.static_folder_images, 'classified_images')
            subfolder_names = ['human','non_human','combined','human_2','non_human_2','combined_2']

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
                    


    # def split_images(self, img: np.ndarray, x_break: int, y_break: int, k: str):
    #     # print("inside split_images")
    #     # set_global(str(x_break))
    #     # print("globaldimension",global_dimension)
        
    #     height, width, depth = img.shape
    #     s_height = ceil(height / y_break)
    #     s_width = ceil(width / x_break)

    #     output_dir = os.path.join(self.static_folder_images, 'split_images')
    #     # if os.path.exists(output_dir):  # Using os.path.exists instead of genericpath.exists for consistency
    #     #     shutil.rmtree(output_dir)
    #     # if not os.path.exists(output_dir):
    #     #     os.mkdir(output_dir)

    #     # for k1 in range(session['num_of_images']):
    #     for i in range(y_break):
    #         for j in range(x_break):
    #             temp = img[i * s_height:(i + 1) * s_height, j * s_width:(j + 1) * s_width]
    #             cv2.imwrite("{}/{}_{}_{}.png".format(output_dir, k,i, j), temp)
        
    #     return output_dir

    def split_images(self, img: np.ndarray, x_break: int, y_break: int, k: str, folder_name):
        # print("inside split_images")
        # set_global(str(x_break))
        # print("globaldimension",global_dimension)
        
        height, width, depth = img.shape
        s_height = ceil(height / y_break)
        s_width = ceil(width / x_break)

        output_dir = os.path.join(self.static_folder_images, folder_name)
        # if os.path.exists(output_dir):  # Using os.path.exists instead of genericpath.exists for consistency
        #     shutil.rmtree(output_dir)
        # if not os.path.exists(output_dir):
        #     os.mkdir(output_dir)

        # for k1 in range(session['num_of_images']):
        for i in range(y_break):
            for j in range(x_break):
                temp = img[i * s_height:(i + 1) * s_height, j * s_width:(j + 1) * s_width]
                cv2.imwrite("{}/{}_{}_{}.png".format(output_dir, k,i, j), temp)
        
        return output_dir

    def image_splitter(self, data,folder_name):
        base64_decoded = base64.b64decode(data["image"])
        img = Image.open(io.BytesIO(base64_decoded))
        temp = np.array(img)
        image_np = np.zeros_like(temp)
        image_np[:,:,0] = temp[:,:,2]
        image_np[:,:,1] = temp[:,:,1]
        image_np[:,:,2] = temp[:,:,0]
        print(type(img))
        out_fol = self.split_images(image_np, int(data['x_size']), int(data['y_size']), data['image_name'],folder_name)
        return out_fol


# from PIL import Image
# import base64
# from genericpath import exists
# from math import ceil
# import shutil
# import os
# import cv2
# import numpy as np
# from scripts.constants.global_constants import STATIC_FOLDER_IMAGES
# import io

# # c:\Users\saija\Desktop\imgclass\portal\./img_static



# def check_folder():
#     folder_name = os.path.join(STATIC_FOLDER_IMAGES, 'split_images')
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#     else:
#         for f in os.listdir(folder_name):
#             item_path = os.path.join(folder_name, f)
#             os.remove(item_path)


# def split_images(img: np.ndarray, x_break: int, y_break: int,k : str):
#     print("inside split_images")
#     # print(STATIC_FOLDER)

#     height, width, depth = img.shape
#     s_height = ceil(height / y_break)
#     s_width = ceil(width / x_break)
    
    
#     output_dir = os.path.join(STATIC_FOLDER_IMAGES, 'split_images')
#     if exists(output_dir): shutil.rmtree(output_dir)
#     if not exists(output_dir) : os.mkdir(output_dir)

#     for i in range(y_break):
#         for j in range(x_break):
#             temp = img[i * s_height:(i + 1) * s_height, j * s_width:(j + 1) * s_width]
            
#             #white_pix = len(np.where(temp == 255)[0])
#             cv2.imwrite("{}/{}_{}.png".format(output_dir, i, j), temp)
             
#     return output_dir

# def image_splitter(data):
#     base64_decoded = base64.b64decode(data["image"])
#     img = Image.open(io.BytesIO(base64_decoded))
#     image_np = np.array(img)
#     print(type(img))
#     out_fol = split_images(image_np,int(data['x_size']),int(data['y_size']),data['image_name'])
#     return out_fol
