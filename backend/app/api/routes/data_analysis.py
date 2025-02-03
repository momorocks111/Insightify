from flask_restx import Resource, Namespace
from app.services.data_preprocessing import DataPreprocessor
from flask import request
import logging
import pandas as pd

logger = logging.getLogger(__name__)

ns = Namespace('analysis', description='Data analysis operations')

# Initialize the DataPreprocessor once
preprocessor = DataPreprocessor()

@ns.route('/preprocess')
class DataPreprocessing(Resource):
    def post(self):
        """Preprocess data"""
        try:
            data = request.json['data']
            df = pd.DataFrame(data)
            
            # Check if the DataFrame is empty
            if df.empty:
                return {'error': 'Empty dataset provided'}, 400
            
            # Check if there are any categorical columns
            categorical_columns = df.select_dtypes(include=['object', 'category']).columns
            if len(categorical_columns) == 0:
                # If no categorical columns, just return the original data
                return {'message': 'No preprocessing needed', 'result': df.to_dict(orient='records')}, 200
            
            if not preprocessor.is_fitted:
                result = preprocessor.fit_transform(df)
            else:
                result = preprocessor.transform(df)
            return {'message': 'Data preprocessed successfully', 'result': result.to_dict(orient='records')}, 200
        except Exception as e:
            logger.error(f"Error preprocessing data: {str(e)}")
            return {'error': str(e)}, 400
