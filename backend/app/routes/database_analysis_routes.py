import os
import json
from flask import Blueprint, request, jsonify, current_app
from app.services.file_service import process_file
from app.services.analysis_service import analyze_dataframe, analyze_sql_statements, analyze_sqlite_database
from app.utils.logger import logger
import pandas as pd

database_analysis_routes = Blueprint('database_analysis', __name__)

@database_analysis_routes.route('/api/database_analysis', methods=['POST'])
def analyze_database():
    logger.info("Entering analyze_database function")
    if 'file' not in request.files:
        logger.error("No file part in the request")
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    logger.info(f"Received file: {file.filename}")

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
            
            if isinstance(data, pd.DataFrame):
                logger.info(f"DataFrame shape: {data.shape}")
                analysis_results = analyze_dataframe(data)
                file_type = 'DataFrame'
            elif isinstance(data, list):  # SQL statements
                logger.info(f"Number of SQL statements: {len(data)}")
                analysis_results = analyze_sql_statements(data)
                file_type = 'list'
            elif isinstance(data, dict):  # SQLite database
                logger.info(f"Number of tables: {len(data)}")
                analysis_results = analyze_sqlite_database(data)
                file_type = 'dict'
            else:
                raise ValueError("Unsupported data format")
            
            logger.info("Data processed and analyzed")
            
            response = jsonify({
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
