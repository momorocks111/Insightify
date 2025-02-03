from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.services.file_processing import FileProcessor
import os
import logging

logger = logging.getLogger(__name__)

file_upload = Blueprint('file_upload', __name__)
file_processor = FileProcessor()

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@file_upload.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.error("No file part in the request")
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        logger.error("No file selected for uploading")
        return jsonify({"error": "No file selected"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        try:
            result = file_processor.process_file(file_path)
            logger.info(f"File processed successfully: {filename}")
            return jsonify({"message": "File processed successfully", "data": result.to_dict() if isinstance(result, pd.DataFrame) else result}), 200
        except Exception as e:
            logger.error(f"Error processing file {filename}: {str(e)}")
            return jsonify({"error": str(e)}), 500
