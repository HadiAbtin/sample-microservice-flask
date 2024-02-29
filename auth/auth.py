from flask import Flask
from auth.config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config)
    return app
