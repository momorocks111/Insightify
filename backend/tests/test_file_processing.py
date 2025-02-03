import unittest
from pathlib import Path
from app.services.file_processing import FileProcessor
import pandas as pd
import sqlite3
import os

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.file_processor = FileProcessor()
        self.test_files_dir = Path('tests/test_files')
        self.test_files_dir.mkdir(exist_ok=True)

    def test_process_csv(self):
        csv_path = self.test_files_dir / 'test.csv'
        pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}).to_csv(csv_path, index=False)
        result = self.file_processor.process_file(csv_path)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 2))

    def test_process_excel(self):
        excel_path = self.test_files_dir / 'test.xlsx'
        pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}).to_excel(excel_path, index=False)
        result = self.file_processor.process_file(excel_path)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(result.shape, (3, 2))

    def test_process_sqlite(self):
        db_path = self.test_files_dir / 'test.db'
        conn = sqlite3.connect(db_path)
        pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}).to_sql('test_table', conn, index=False)
        conn.close()
        result = self.file_processor.process_file(db_path)
        self.assertIsInstance(result, dict)
        self.assertIn('test_table', result)
        self.assertIsInstance(result['test_table'], pd.DataFrame)
        self.assertEqual(result['test_table'].shape, (3, 2))

    def tearDown(self):
        for file in self.test_files_dir.iterdir():
            file.unlink()
        self.test_files_dir.rmdir()

if __name__ == '__main__':
    unittest.main()
