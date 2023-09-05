from flask import Blueprint, render_template, request, jsonify, url_for
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.make_prediction_handler import ClassifyImages

split_images_bp = Blueprint('split_images_bp',__name__)

@split_images_bp.route('/split_images',methods=["GET","POST"])
def splitimage():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'split_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        return render_template("split_images.html", images=image_files,split_type=num_of_images)
    elif request.method == "POST":
        make_prediction_object = ClassifyImages()
        make_prediction_object.classify_images()
        # data = request.json
        #redirect_url = url_for('apply_saliency_bp.saliency') 
        redirect_url = url_for('make_prediction_bp.make_prediction')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})


