from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES

saliecy_bp = Blueprint('saliency_bp',__name__)

@saliecy_bp.route('/apply_saliency',methods=["GET","POST"])
def saliency():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'split_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        return render_template("apply_saliency.html", images=image_files)
    

# @bp.route('/page2', methods=["GET", "POST"])
# def page2():
#     if request.method == "GET":
#         # Get list of all image files from folder1
#         image_folder = 'sai'
#         image_files = [f for f in os.listdir(os.path.join(bp.static_folder,'images', 'sai')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
#         # print(image_files)
#         return render_template("page2.html", images=image_files)