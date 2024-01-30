import numpy as np
import os
from PIL import Image
import cv2
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES
# from constants import dir_path, output_path_dir, img_split_dim, file_name

class ImageReconstructor:
    def __init__(self,saliency_path,reconstructed_path,input_split_dimension = None):
        self.proj_dir = STATIC_FOLDER_IMAGES
        self.dir_path = os.path.join(self.proj_dir, saliency_path)
        self.img_split_dim = input_split_dimension
        self.output_path_dir = os.path.join(self.proj_dir, reconstructed_path)
        self.file_name = "reconstructed_image"
        

    # def reconstruct_images(self):
    #     file_list = os.listdir(self.dir_path)

    #     max_color = (0, 0, 0)
    #     x = np.asarray(Image.open(os.path.join(self.dir_path, file_list[0])))
    #     req_shape = x.shape

    #     op_im = np.zeros((1920, 1920, 3), dtype=np.uint8)
    #     dim_patch = int(1920 // self.img_split_dim)

    #     for each_file in file_list:
    #         im = cv2.imread(os.path.join(self.dir_path, each_file))
    #         fname = each_file[:-4]
    #         pos = fname.split('_')  # position
    #         pos = list(map(int, pos))
    #         assert im.ndim == 3
    #         op_im[pos[0] * (dim_patch):(pos[0] + 1) * (dim_patch), pos[1] * (dim_patch):(pos[1] + 1) * (dim_patch), :] = im

    #     final_comb_image = Image.fromarray(op_im)
    #     final_comb_image.save(os.path.join(self.output_path_dir, 'File_{}.png'.format(str(self.file_name).zfill(2))))

    def reconstruct_images(self):
        file_list = os.listdir(self.dir_path)

        max_color = (0, 0, 0)
        x = np.asarray(Image.open(os.path.join(self.dir_path, file_list[0])))
        req_shape = x.shape

        op_im = np.zeros((1920, 1920, 3), dtype=np.uint8)
        dim_patch = int(1920 // self.img_split_dim)

        for each_file in file_list:
            im = cv2.imread(os.path.join(self.dir_path, each_file))
            fname = each_file[:-4]
            pos = fname.split('_')  # position
            pos = list(map(int, pos))
            assert im.ndim == 3
            
            # Resize im to match the shape of the slice in op_im
            im = cv2.resize(im, (dim_patch, dim_patch))
            
            op_im[
                # pos[0] * dim_patch : (pos[0] + 1) * dim_patch,
                pos[1] * dim_patch : (pos[1] + 1) * dim_patch,
                pos[2] * dim_patch : (pos[2] + 1) * dim_patch
                :
            ] = im

        final_comb_image = Image.fromarray(op_im)
        final_comb_image.save(os.path.join(self.output_path_dir, 'File_{}.png'.format(str(self.file_name).zfill(2))))

        # ... (rest of your code)

    # def reconstruct_images(self):
    #     file_list = os.listdir(self.dir_path)

    #     max_color = (0, 0, 0)
    #     x = np.asarray(Image.open(os.path.join(self.dir_path, file_list[0])))
    #     req_shape = x.shape

    #     op_im = np.zeros((1920, 1920, 3), dtype=np.uint8)
    #     dim_patch = int(1920 // self.img_split_dim)

    #     for each_file in file_list:
    #         im = cv2.imread(os.path.join(self.dir_path, each_file))
    #         fname = each_file[:-4]  # Remove the file extension '.png'
    #         pos = fname.split('_')  # position
    #         print(pos)
    #         pos = list(map(int, pos))
    #         assert im.ndim == 3
            
    #         # Adjust to handle the new file naming convention
    #         if len(pos) == 3:  # Ensure the filename follows the new convention
    #             im = cv2.resize(im, (dim_patch, dim_patch))
                
    #             # Check if the position indices fall within the bounds of op_im
    #             if (
    #                 0 <= pos[0] * dim_patch < 1920 and
    #                 0 <= pos[1] * dim_patch < 1920 and
    #                 0 <= (pos[0] + 1) * dim_patch <= 1920 and
    #                 0 <= (pos[1] + 1) * dim_patch <= 1920
    #             ):
    #                 op_im[
    #                     pos[0] * dim_patch : (pos[0] + 1) * dim_patch,
    #                     pos[1] * dim_patch : (pos[1] + 1) * dim_patch,
    #                     :
    #                 ] = im

    #     final_comb_image = Image.fromarray(op_im)
    #     final_comb_image.save(os.path.join(self.output_path_dir, 'File_{}.png'.format(str(self.file_name).zfill(2))))
