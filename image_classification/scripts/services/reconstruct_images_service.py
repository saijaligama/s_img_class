from flask import Blueprint, render_template, request, jsonify, url_for,session
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.skeleton_handler import SkeletonProcessor
reconstruct_images_bp = Blueprint('reconstruct_images_bp',__name__)

@reconstruct_images_bp.route('/reconstruct_images',methods = ["GET","POST"])
def recon_images():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'Reconstructed_Images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        if session['num_of_images'] == 1:
            return render_template("reconstruct_images.html", 
                               images=image_files,split_type=num_of_images)
        else:
            image_files2 = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'Reconstructed_Images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            return render_template("reconstruct_images_2.html", 
                               images=image_files,images2=image_files2,split_type=num_of_images)
    elif request.method == "POST":
        skeleton_object = SkeletonProcessor('Reconstructed_Images','skeleton_temp')
        skeleton_object.process_image(session['image_name_0'])
        if session['num_of_images'] == 2:
            skeleton_object2 = SkeletonProcessor('Reconstructed_Images_2','skeleton_temp_2')
            skeleton_object2.process_image(session['image_name_1'])
        redirect_url = url_for('skeleton_bp.skeleton')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})

