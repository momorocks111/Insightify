import unittest
from app import create_app
import io
import json

class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_file_upload(self):
        data = {'file': (io.BytesIO(b"x,y\n1,2\n3,4\n"), 'sample.csv')}
        response = self.client.post('/file/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('message', response_data)
        self.assertIn('result', response_data)

    def test_data_preprocessing_with_categorical(self):
        data = {'data': [{'x': 1, 'y': 'A'}, {'x': 3, 'y': 'B'}]}
        response = self.client.post('/analysis/preprocess', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('message', response_data)
        self.assertIn('result', response_data)

    def test_data_preprocessing_without_categorical(self):
        data = {'data': [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]}
        response = self.client.post('/analysis/preprocess', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('message', response_data)
        self.assertIn('result', response_data)

    def test_visualization_generation(self):
        data = {
            'data': {'x': [1, 2, 3], 'y': [4, 5, 6]},
            'type': 'line',
            'x_column': 'x',
            'y_column': 'y',
            'title': 'Test Visualization'
        }
        response = self.client.post('/visualization/generate', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('plot', response_data)
        self.assertIn('type', response_data)

if __name__ == '__main__':
    unittest.main()
