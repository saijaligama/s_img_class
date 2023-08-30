from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global

saliecy_bp = Blueprint('saliency_bp',__name__)

@saliecy_bp.route('/apply_saliency',methods=["GET","POST"])
def saliency():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'split_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        print("len of images",num_of_images)
        # x=get_global()
        # print("getglobal",x)
        return render_template("apply_saliency.html", images=image_files,split_type=num_of_images)
    

