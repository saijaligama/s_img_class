from flask import Flask
from scripts.services import home_Service 
from scripts.services import split_images_service
from scripts.services import make_prediction_service
from scripts.services import apply_saliency_service

app = Flask(__name__)

app.register_blueprint(home_Service.home)
app.register_blueprint(split_images_service.split_images_bp)
app.register_blueprint(make_prediction_service.make_prediction_bp)
app.register_blueprint(apply_saliency_service.apply_saliency_bp)

if __name__ == "__main__":
    app.run(port=8009)