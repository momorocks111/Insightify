from flask import Flask
from app.api.routes.file_upload import file_upload
from app.core.logging import setup_logging

def create_app():
    app = Flask(__name__)
    setup_logging()
    
    app.register_blueprint(file_upload, url_prefix='/api')
    
    return app
