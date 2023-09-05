#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
from PIL import Image


# In[21]:


# The below are inputs for the code
dir_path = r'C:\Users\jahna\OneDrive\Documents\GitHub\Project\Image_Filter_Reconstruction\Reconstructed_Images'
img_split_dim = 8
# The below are inputs for the code
output_path_dir = r'C:/Users/jahna/OneDrive/Documents/GitHub/Project/Image_Filter_Reconstruction/Output Images'

file_list = os.listdir(dir_path)


# In[31]:


max_color = (0, 0, 0)
x = np.asarray(Image.open(os.path.join(dir_path, file_list[0])))
req_shape = x.shape
print(req_shape)


# In[32]:


files = {}
for each_file in file_list:
    file_num, row, col = list(map(int, each_file.split('.')[0].split('_')))
    if file_num not in files:
        files[file_num] = np.zeros([img_split_dim, img_split_dim], dtype = object)
    files[file_num][row][col] = os.path.join(dir_path, each_file)


# In[33]:


# max_color = tuple([x//100 for x in max_color])
for file_name, file_matrix in files.items():
    imgs_comb_v = []
    for ind, file_row in enumerate(file_matrix):
        imgs_comb_h = []
        for each_val in file_row:
            if each_val != 0:
                imgs_comb_h.append(Image.open(each_val))
            else:
                imgs_comb_h.append(Image.new('RGBA', req_shape[:2], color=max_color))
#         print(type(np.hstack(imgs_comb_h)))
        imgs_comb_v.append(np.hstack(imgs_comb_h))
#         print(type(imgs_comb_v[ind]))
    final_comb_image = np.vstack(imgs_comb_v)
    final_comb_image = Image.fromarray(final_comb_image)
    final_comb_image.save(os.path.join(output_path_dir, 'File_{}.png'.format(str(file_name).zfill(2))))


# In[ ]:




