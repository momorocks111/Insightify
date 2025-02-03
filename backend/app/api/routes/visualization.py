from flask_restx import Namespace, Resource
from flask import request
from app.services.visualization import Visualizer
import pandas as pd
import logging

logger = logging.getLogger(__name__)

ns = Namespace('visualization', description='Data visualization operations')

visualizer = Visualizer()

@ns.route('/generate')
class VisualizationGenerator(Resource):
    def post(self):
        """Generate a visualization"""
        try:
            data = request.json
            df = pd.DataFrame(data['data'])
            result = visualizer.generate_visualization(df, data['type'], data['x_column'], data['y_column'], data.get('title', ''))
            return result, 200
        except Exception as e:
            logger.error(f"Error generating visualization: {str(e)}")
            return {'error': str(e)}, 400
