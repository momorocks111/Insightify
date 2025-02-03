from flask_restx import Api
from .file_upload import ns as file_ns
from .data_analysis import ns as analysis_ns
from .visualization import ns as viz_ns

api = Api(
    title='Insightify API',
    version='1.0',
    description='A data analysis and visualization API',
)

api.add_namespace(file_ns, path='/file')
api.add_namespace(analysis_ns, path='/analysis')
api.add_namespace(viz_ns, path='/visualization')
