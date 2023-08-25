from flask import Flask
from scripts.services import home_Service 
from scripts.services import apply_saliency_service

app = Flask(__name__)

app.register_blueprint(home_Service.home)
app.register_blueprint(apply_saliency_service.saliecy_bp)

if __name__ == "__main__":
    app.run(port=8009)