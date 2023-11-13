from flask import Blueprint, render_template, request, jsonify, url_for, session
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.make_prediction_handler import ClassifyImages

split_images_bp = Blueprint('split_images_bp',__name__)

@split_images_bp.route('/split_images',methods=["GET","POST"])
def splitimage():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'split_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))

        if session['num_of_images'] == 1:
            return render_template("split_images.html", images=image_files,split_type=num_of_images)
        else:
            image_files2 = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'split_images_2')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            num_of_images2 = str(int(len(image_files)**0.5))
            return render_template("split_images_2.html", images=image_files,images2 = image_files2,split_type=num_of_images)
    
    elif request.method == "POST":
        input_split_dimension = session['image_split_dimension']
        make_prediction_object = ClassifyImages('split_images',input_split_dimension = int(input_split_dimension))
        make_prediction_object.classify_images(session['image_name_0'],'human','combined')
        if session['num_of_images'] == 2: 
            make_prediction_object2 = ClassifyImages('split_images_2',input_split_dimension = int(input_split_dimension))
            make_prediction_object2.classify_images(session['image_name_1'],'human_2','combined_2')

            # data = request.json
            #redirect_url = url_for('apply_saliency_bp.saliency') 
        redirect_url = url_for('make_prediction_bp.make_prediction')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})
        


