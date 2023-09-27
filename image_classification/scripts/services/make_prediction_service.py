from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import CLASSIFIED_IMAGES, STATIC_FOLDER_IMAGES
from scripts.core.handlers.apply_saleincy_handler import ApplySaliency
make_prediction_bp = Blueprint('make_prediction_bp',__name__)




@make_prediction_bp.route('/make_prediction',methods=["GET","POST"])
def make_prediction():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(CLASSIFIED_IMAGES, 'human')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        non_image_files = [f for f in os.listdir(os.path.join(CLASSIFIED_IMAGES, 'non_human')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        print(os.path.join(CLASSIFIED_IMAGES, 'human'))
        # num_of_images = str(int(len(image_files)**0.5))
        # non_num_of_images
        return render_template("make_prediction.html", images=image_files,non_images = non_image_files,split_type='8')
    elif request.method == "POST":
        saliency_object = ApplySaliency()
        saliency_object.process_images()
        redirect_url = url_for('apply_saliency_bp.apply_saliency')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})
