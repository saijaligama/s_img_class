from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.reconstruct_images_handler import ImageReconstructor
apply_saliency_bp = Blueprint('apply_saliency_bp',__name__)

@apply_saliency_bp.route('/apply_saliency',methods=["GET","POST"])
def apply_saliency():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'saliency_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        print("len of images",num_of_images)
        # x=get_global()
        # print("getglobal",x)
        return render_template("apply_saliency.html", images=image_files,split_type=num_of_images)
    elif request.method == "POST":
        reconstruction_object = ImageReconstructor()
        reconstruction_object.reconstruct_images()
        redirect_url = url_for('reconstruct_images_bp.recon_images')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})

    
    

