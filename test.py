import cv2
import numpy as np
from tensorflow.keras.saving import load_model
import os
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import model_from_json
from tensorflow.keras.losses import SparseCategoricalCrossentropy


output_dir1 = r"C:\Users\saija\Desktop\imgclass\trails\1"
#output_dir1 = "./image_classification/static/images/split_images"
#os.path.join(output_dir, str(k))  

#json_path = "./image_classification/static/cnn_models/model.json"
#weights_path = "./image_classification/static/cnn_models/model.h5"

#def _load_model(json_path, weights_path):
#        with open(json_path, 'r') as json_file:
#            loaded_model_json = json_file.read()
#        loaded_model = model_from_json(loaded_model_json)
#        loaded_model.load_weights(weights_path)
#        return loaded_model
        
for j in range(int(8)): 
    for i in range(int(8)):
        new = "{}/{}_{}.png".format(output_dir1,j,i)
        img = cv2.imread(new)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img2 = cv2.resize(img2, (120, 120))
        #img2 = cv2.resize(img2, (240, 240))
        img2 = np.array(img2)
        img2 = np.expand_dims(img2, axis=0)
        #########################################################3
        #model = _load_model(json_path,weights_path)
        #model.compile(optimizer='adam',
        #            loss=SparseCategoricalCrossentropy(from_logits=True),
        #             metrics=['accuracy'])
        ##############################################################
        model = load_model('./image_classification/static/cnn_models/cnn.h5', compile=False)
        prediction = model.predict(img2)
        print("prediction",prediction)
        print(new)
     
        if (prediction > 0.2) :
        #if prediction[0][0] > 0.2:
            output_dir_human = os.path.join(output_dir1, 'Human')
            if not os.path.exists(output_dir_human) : os.mkdir(output_dir_human)
             
            cv2.imwrite("{}/{}_{}.png".format(output_dir_human,j,i), img)
        else :
            output_dir_non_human = os.path.join(output_dir1, 'Non_human')
            if not os.path.exists(output_dir_non_human) : os.mkdir(output_dir_non_human)
            cv2.imwrite("{}/{}_{}.png".format(output_dir_non_human, j, i), img)
 