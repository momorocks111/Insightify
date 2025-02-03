from flask import Flask
from .api.routes import api
from .core.logging import setup_logging
from .services.model_management import ModelManager

def create_app():
    app = Flask(__name__)
    setup_logging()
    
    # Initialize ModelManager
    app.model_manager = ModelManager()
    
    api.init_app(app)
    
    return app
