from flask import Flask
from scripts.services import home_Service 
from scripts.services import split_images_service
from scripts.services import make_prediction_service
from scripts.services import apply_saliency_service
from scripts.services import skeleton_service
from scripts.services import reconstruct_images_service
from scripts.services import correlation_service

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(home_Service.home)
app.register_blueprint(split_images_service.split_images_bp)
app.register_blueprint(make_prediction_service.make_prediction_bp)
app.register_blueprint(apply_saliency_service.apply_saliency_bp)
app.register_blueprint(skeleton_service.skeleton_bp)
app.register_blueprint(reconstruct_images_service.reconstruct_images_bp)
app.register_blueprint(correlation_service.correlation_bp)

if __name__ == "__main__":
    app.run(port=8009)
