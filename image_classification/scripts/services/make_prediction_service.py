from flask import Blueprint, render_template, request, jsonify, url_for, session
import os
from scripts.constants.global_constants import CLASSIFIED_IMAGES, STATIC_FOLDER_IMAGES
from scripts.core.handlers.apply_saleincy_handler import ApplySaliency
make_prediction_bp = Blueprint('make_prediction_bp',__name__)




@make_prediction_bp.route('/make_prediction',methods=["GET","POST"])
def make_prediction():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(CLASSIFIED_IMAGES, 'combined')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        if session['num_of_images'] == 1:
            return render_template("make_prediction.html", images=image_files,split_type=num_of_images)
        else:
            image_files2 = [f for f in os.listdir(os.path.join(CLASSIFIED_IMAGES, 'combined_2')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            num_of_images2 = str(int(len(image_files)**0.5))
            return render_template("make_prediction_2.html", images=image_files,images2 =image_files2, split_type=num_of_images)

    elif request.method == "POST":
        saliency_object = ApplySaliency("human")
        saliency_object.process_images('saliency_images')
        if session['num_of_images'] == 2:
            saliency_object2 = ApplySaliency("human_2")
            saliency_object2.process_images('saliency_images_2')
            
        redirect_url = url_for('apply_saliency_bp.apply_saliency')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})
