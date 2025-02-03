from flask import Blueprint, request, jsonify
from backend.app.utils.data_processing import process_file
from models.model import train_model

api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        data = process_file(file)
        # Assuming data is processed and split into X and y
        train_model(data['X'], data['y'])
        return jsonify({'message': 'File processed and model trained'}), 200
