from app.core.logging import setup_logging
from app.services.file_processing import FileProcessor
from pathlib import Path

def main():
    setup_logging()
    
    # Example usage
    file_processor = FileProcessor()
    
    # You would typically get this path from the frontend
    sample_file_path = Path('path/to/your/sample/file.csv')
    
    try:
        result = file_processor.process_file(sample_file_path)
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
