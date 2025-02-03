import logging
from pathlib import Path
import pandas as pd
import sqlite3
import PyPDF2
import openpyxl

logger = logging.getLogger(__name__)

class FileProcessor:
    def __init__(self):
        self.supported_extensions = {'.pdf', '.xlsx', '.csv', '.db', '.sqlite'}

    def process_file(self, file_path: Path):
        if not isinstance(file_path, Path):
            file_path = Path(file_path)
        
        if file_path.suffix not in self.supported_extensions:
            logger.error(f"Unsupported file type: {file_path.suffix}")
            raise ValueError(f"Unsupported file type: {file_path.suffix}")

        logger.info(f"Processing file: {file_path}")
        
        if file_path.suffix == '.pdf':
            return self._process_pdf(file_path)
        elif file_path.suffix == '.xlsx':
            return self._process_excel(file_path)
        elif file_path.suffix == '.csv':
            return self._process_csv(file_path)
        elif file_path.suffix in {'.db', '.sqlite'}:
            return self._process_sqlite(file_path)

    def _process_pdf(self, file_path: Path):
        logger.info(f"Processing PDF file: {file_path}")
        text_content = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_content += page.extract_text()
        return pd.DataFrame({'content': [text_content]})

    def _process_excel(self, file_path: Path):
        logger.info(f"Processing Excel file: {file_path}")
        return pd.read_excel(file_path)

    def _process_csv(self, file_path: Path):
        logger.info(f"Processing CSV file: {file_path}")
        return pd.read_csv(file_path)

    def _process_sqlite(self, file_path: Path):
        logger.info(f"Processing SQLite file: {file_path}")
        conn = sqlite3.connect(file_path)
        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
        result = {}
        for table_name in tables['name']:
            result[table_name] = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return result
