import unittest
import pandas as pd
import numpy as np
from app.services.data_preprocessing import DataPreprocessor

class TestDataPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = DataPreprocessor()
        self.sample_data = pd.DataFrame({
            'numeric_col': [1, 2, np.nan, 4, 5],
            'categorical_col': ['A', 'B', 'C', 'A', np.nan]
        })

    def test_fit_transform(self):
        transformed_data = self.preprocessor.fit_transform(self.sample_data)
        self.assertIsInstance(transformed_data, pd.DataFrame)
        self.assertEqual(transformed_data.shape[0], self.sample_data.shape[0])
        self.assertGreater(transformed_data.shape[1], self.sample_data.shape[1])

    def test_transform(self):
        self.preprocessor.fit_transform(self.sample_data)
        new_data = pd.DataFrame({
            'numeric_col': [6, np.nan, 8],
            'categorical_col': ['B', 'D', 'A']
        })
        transformed_data = self.preprocessor.transform(new_data)
        self.assertIsInstance(transformed_data, pd.DataFrame)
        self.assertEqual(transformed_data.shape[0], new_data.shape[0])

if __name__ == '__main__':
    unittest.main()
