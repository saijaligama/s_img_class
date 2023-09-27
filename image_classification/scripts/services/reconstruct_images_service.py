from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.skeleton_handler import SkeletonProcessor
reconstruct_images_bp = Blueprint('reconstruct_images_bp',__name__)

@reconstruct_images_bp.route('/reconstruct_images',methods = ["GET","POST"])
def recon_images():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'Reconstructed_Images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        print("len of images",num_of_images)
        # x=get_global()
        # print("getglobal",x)
        return render_template("reconstruct_images.html", 
                               images=image_files,split_type=num_of_images)
    elif request.method == "POST":
        skeleton_object = SkeletonProcessor()
        skeleton_object.process_image()
        redirect_url = url_for('skeleton_bp.skeleton')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})

