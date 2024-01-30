from flask import Blueprint, render_template, request, jsonify, url_for, session
import os
import io
from PIL import Image
from genericpath import exists
from math import ceil
import shutil
import cv2
from scripts.core.handlers.split_images_handler import ImageProcessor
import base64
import numpy as np
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, set_global


home = Blueprint('home', __name__)
            
@home.route('/',methods=["GET","POST"])
def home_page():
    image_processor = ImageProcessor()
    if request.method == "GET":
        image_processor.check_folder()
        return render_template("home.html")
    
    try:
        if request.method == "POST":
            image_processor2 = ImageProcessor()
            data = request.json
            session['image_split_dimension'] = data['images'][0]['x_size']
            session['num_of_images'] = len(data['images'])

            session['image_name_0'] = data['images'][0]['image_name']
            base64_decoded = base64.b64decode(data['images'][0]["image"])
            img = Image.open(io.BytesIO(base64_decoded))
            out_path = os.path.join(STATIC_FOLDER_IMAGES,'uploaded_images')
            img.save("{}/{}.{}".format(out_path,data['images'][0]['image_name'],'png'))

            # image_processor2.save_image(data['images'][0])

            result = image_processor.image_splitter(data['images'][0],'split_images')
            

            if session['num_of_images'] == 2:  
                session['image_name_1'] = data['images'][1]['image_name']
                base64_decoded = base64.b64decode(data['images'][1]["image"])
                img = Image.open(io.BytesIO(base64_decoded))
                out_path = os.path.join(STATIC_FOLDER_IMAGES,'uploaded_images')
                img.save("{}/{}.{}".format(out_path,data['images'][1]['image_name'],'png'))


                result_1 = image_processor.image_splitter(data['images'][1],'split_images_2')
                # image_processor.save_image(data['images'][1])   

            redirect_url = url_for('split_images_bp.splitimage') 

            return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})
            
    except Exception as e:
        return jsonify({"error": str(e)})
