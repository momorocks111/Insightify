import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_dir: str = 'logs'):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'app.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5),
            logging.StreamHandler()
        ]
    )

    # Suppress some of the more verbose logging from libraries
    logging.getLogger('werkzeug').setLevel(logging.WARNING)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
