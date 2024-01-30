from flask import Blueprint, render_template, request, jsonify, url_for,session
import os
from scripts.constants.global_constants import STATIC_FOLDER_IMAGES, get_global
from scripts.core.handlers.correlation_handler import CorrelationProcessor

correlation_bp = Blueprint('correlation_bp',__name__)

@correlation_bp.route('/correlation',methods=["GET","POST"])
def correlation():
    if request.method == "GET":
        image_files = [f for f in os.listdir(os.path.join(STATIC_FOLDER_IMAGES, 'correlation_images')) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        num_of_images = str(int(len(image_files)**0.5))
        print("len of images",num_of_images)
        return render_template("correlation.html", images=image_files,split_type=num_of_images)
    else:
        data = request.json
        corr_object = CorrelationProcessor()

        corr_object.process_correlation(session['image_name'],float(data['corr_coef']))
        # redirect_url = url_for('correlation_bp.correlation')
        return jsonify({"message": "Image processed successfully!"})