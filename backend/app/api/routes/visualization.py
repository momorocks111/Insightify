from flask import Blueprint, request, jsonify
from app.services.visualization import Visualizer
import pandas as pd
import logging

logger = logging.getLogger(__name__)

visualization = Blueprint('visualization', __name__)
visualizer = Visualizer()

@visualization.route('/generate', methods=['POST'])
def generate_visualization():
    try:
        data = request.json.get('data')
        viz_type = request.json.get('type')
        x_column = request.json.get('x_column')
        y_column = request.json.get('y_column')
        title = request.json.get('title', '')

        df = pd.DataFrame(data)
        
        if not viz_type:
            viz_type = visualizer.suggest_visualization(df)

        result = visualizer.generate_visualization(df, viz_type, x_column, y_column, title)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error in generate_visualization: {str(e)}")
        return jsonify({"error": str(e)}), 400

