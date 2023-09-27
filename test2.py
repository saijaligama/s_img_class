#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
from PIL import Image
import cv2


# In[21]:


# The below are inputs for the code
dir_path = r'C:\Users\saija\Desktop\Sharma\image_classification\static\images\saliency_images'
img_split_dim = 8
# The below are inputs for the code
output_path_dir = r'C:\Users\saija\Desktop\Sharma\image_classification\static\images\Reconstructed_Images'

file_list = os.listdir(dir_path)


# In[31]:


max_color = (0, 0, 0)
x = np.asarray(Image.open(os.path.join(dir_path, file_list[0])))
req_shape = x.shape
print(req_shape)


# In[32]:
print(file_list)

#files = {}
#for each_file in file_list:
#    file_num, row, col = list(map(int, each_file.split('.')[0].split('_')))
#    if file_num not in files:
#        files[file_num] = np.zeros([img_split_dim, img_split_dim], dtype = object)
#    files[file_num][row][col] = os.path.join(dir_path, each_file)
   

op_im = np.zeros((1920,1920,3),dtype=np.uint8)

dim_patch = int(1920//img_split_dim)

for each_file in file_list:
    im = cv2.imread(os.path.join(dir_path, each_file)) 
    fname = each_file[:-4]
    pos = fname.split('_') #position
    pos = list(map(int,pos))
    assert im.ndim == 3
    op_im[pos[0]*(dim_patch):(pos[0]+1)*(dim_patch),pos[1]*(dim_patch):(pos[1]+1)*(dim_patch),:] = im

final_comb_image = Image.fromarray(op_im)
file_name = 'sharma'
final_comb_image.save(os.path.join(output_path_dir, 'File_{}.png'.format(str(file_name).zfill(2)))) 


    
"""


    
files = {}
for each_file in file_list:
    split_values = each_file.split('.')[0].split('_')
    if len(split_values) == 2:
        file_num, row = list(map(int, split_values))
        col = 0  # if you don't have a column value, you can set it to a default, e.g., 0
        if file_num not in files:
            files[file_num] = np.zeros([img_split_dim, img_split_dim], dtype=object)
        files[file_num][row][col] = os.path.join(dir_path, each_file)
    else:
        print(f"Skipped file due to incorrect naming format: {each_file}")



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


"""

