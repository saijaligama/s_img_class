from flask import Blueprint, render_template, request, jsonify, url_for,session
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.correlation_handler import CorrelationProcessor

skeleton_bp = Blueprint('skeleton_bp',__name__)

@skeleton_bp.route('/skeleton',methods=["GET","POST"])
def skeleton():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'skeleton_temp')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        print("len of images",num_of_images)
        if session['num_of_images'] == 1:
            return render_template("skeleton.html", images=image_files,split_type=num_of_images)
        else:
            image_files2 = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'skeleton_temp_2')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            return render_template("skeleton_2.html", images=image_files,images2=image_files2,split_type=num_of_images)

    else:
        data = request.json
        if session['num_of_images'] == 1:

            corr_object = CorrelationProcessor()

            corr_object.process_correlation(session['image_name_0'],data['corr_coef'])
        else:
            corr_object2 = CorrelationProcessor()
            corr_object2.process_correlation_2(session['image_name_0'],session['image_name_1'])
        redirect_url = url_for('correlation_bp.correlation')
        return jsonify({"message": "Image processed successfully!", "redirect": redirect_url})
    
    

