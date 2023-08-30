from flask import Blueprint, render_template, request, jsonify, url_for
import os
import io
from PIL import Image
from genericpath import exists
from math import ceil
import shutil
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
        return render_template("split_images.html")
    
    try:
        if request.method == "POST":
            data = request.json
            # print(data)
            # set_global(str(data['x_break']))
            result = image_processor.image_splitter(data)
            redirect_url = url_for('saliency_bp.saliency') 
            return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})
    except Exception as e:
        return jsonify({"error": str(e)})
