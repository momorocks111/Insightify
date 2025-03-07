import logging

def setup_logger():
    logger = logging.getLogger('data_analyzer')
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler('data_analyzer.log')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logger()
