from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global

skeleton_bp = Blueprint('skeleton_bp',__name__)

@skeleton_bp.route('/skeleton',methods=["GET","POST"])
def skeleton():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'skeleton_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        print("len of images",num_of_images)
        return render_template("skeleton.html", images=image_files,split_type=num_of_images)
    
    

