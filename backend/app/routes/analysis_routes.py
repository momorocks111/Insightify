import os
import json
from flask import Blueprint, request, jsonify, current_app
from app.services.file_service import process_file
from app.services.analysis_service import analyze_data, analyze_dataframe, analyze_sql_statements, analyze_sqlite_database
from app.services.gemini_service import get_gemini_response
from app.utils.logger import logger
import pandas as pd

analysis_routes = Blueprint('analysis', __name__)

@analysis_routes.route('/api/analyze_with_file', methods=['POST'])
def analyze_with_file():
    logger.info("Entering analyze_with_file function")
    if 'file' not in request.files:
        logger.error("No file part in the request")
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    message = request.form.get('message', '')
    logger.info(f"Received file: {file.filename}, message: {message}")

    if file.filename == '':
        logger.error("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    if file:
        try:
            logger.info("Starting file processing")
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            logger.info(f"Processing {file.filename.split('.')[-1]} file: {file.filename}")
            data = process_file(file, file_path)

            logger.info("File processed. Data type: %s", type(data).__name__)
            logger.info("Data preview: %s", str(data)[:1000])  # Log first 1000 characters of data

            analysis_results = analyze_data(data)
            file_type = type(data).__name__

            logger.info("Data processed and analyzed")
            logger.info("Analysis results: %s", json.dumps(analysis_results, default=str, indent=2))

            logger.info("Preparing data for Gemini API")
            gemini_input = {
                "file_type": file.filename.split('.')[-1],
                "data_type": file_type,
                "analysis_results": analysis_results,
                "user_message": message
            }
            logger.info("Data being sent to Gemini API: %s", json.dumps(gemini_input, default=str, indent=2))

            logger.info("Sending data to Gemini API")
            insights = get_gemini_response("Analyze this data and provide insights.", gemini_input)
            logger.info("Received response from Gemini API")
            logger.info("Gemini response: %s", insights)

            response = jsonify({
                "message": insights,
                "file_info": {
                    'filename': file.filename,
                    'type': file_type,
                    'analysis': analysis_results
                }
            })
            logger.info("Prepared response")
            return response
        except Exception as e:
            logger.error(f"Error processing file: {str(e)}", exc_info=True)
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500

    logger.error("Unknown error occurred")
    return jsonify({'error': 'Unknown error'}), 500

