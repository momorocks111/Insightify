import logging
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, Any

logger = logging.getLogger(__name__)

class Visualizer:
    def __init__(self):
        self.supported_types = ['line', 'bar', 'scatter', 'pie']

    def generate_visualization(self, data: pd.DataFrame, viz_type: str, x_column: str, y_column: str, title: str = '') -> Dict[str, Any]:
        logger.info(f"Generating {viz_type} visualization")
        if viz_type not in self.supported_types:
            logger.error(f"Unsupported visualization type: {viz_type}")
            raise ValueError(f"Unsupported visualization type: {viz_type}")

        try:
            if viz_type == 'line':
                fig = px.line(data, x=x_column, y=y_column, title=title)
            elif viz_type == 'bar':
                fig = px.bar(data, x=x_column, y=y_column, title=title)
            elif viz_type == 'scatter':
                fig = px.scatter(data, x=x_column, y=y_column, title=title)
            elif viz_type == 'pie':
                fig = px.pie(data, names=x_column, values=y_column, title=title)

            return {
                'plot': fig.to_json(),
                'type': viz_type
            }
        except Exception as e:
            logger.error(f"Error generating visualization: {str(e)}")
            raise

    def suggest_visualization(self, data: pd.DataFrame) -> str:
        logger.info("Suggesting visualization type")
        if len(data.select_dtypes(include=['number']).columns) >= 2:
            return 'scatter'
        elif len(data.select_dtypes(include=['number']).columns) == 1:
            return 'bar'
        else:
            return 'pie'

