from flask_restx import Resource, Namespace
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from app.services.file_processing import FileProcessor
import os
import logging
import pandas as pd

logger = logging.getLogger(__name__)

ns = Namespace('file', description='File upload operations')

upload_parser = ns.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@ns.route('/upload')
class FileUpload(Resource):
    @ns.expect(upload_parser)
    def post(self):
        """Upload a file for processing"""
        try:
            args = upload_parser.parse_args()
            uploaded_file = args['file']
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(file_path)
            
            processor = FileProcessor()
            result = processor.process_file(file_path)
            
            if isinstance(result, pd.DataFrame):
                result = result.to_dict(orient='records')
            
            return {'message': 'File processed successfully', 'result': result}, 200
        except Exception as e:
            logger.error(f"Error processing file: {str(e)}")
            return {'error': str(e)}, 400
