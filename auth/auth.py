from flask import Flask, Blueprint
from flask-restful import Api
from auth.config import Config

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config)
    return app
