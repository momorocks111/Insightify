from flask import Flask
from flask_cors import CORS
from config.config import Config
from app.routes.main_routes import main_routes
from app.routes.analysis_routes import analysis_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    app.register_blueprint(main_routes)
    app.register_blueprint(analysis_routes)

    return app
