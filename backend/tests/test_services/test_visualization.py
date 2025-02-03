import unittest
import pandas as pd
from app.services.visualization import Visualizer

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.visualizer = Visualizer()
        self.sample_data = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [2, 4, 6, 8, 10]
        })

    def test_generate_line_chart(self):
        result = self.visualizer.generate_visualization(self.sample_data, 'line', 'x', 'y', 'Test Line Chart')
        self.assertIn('plot', result)
        self.assertEqual(result['type'], 'line')

    def test_generate_bar_chart(self):
        result = self.visualizer.generate_visualization(self.sample_data, 'bar', 'x', 'y', 'Test Bar Chart')
        self.assertIn('plot', result)
        self.assertEqual(result['type'], 'bar')

    def test_generate_scatter_plot(self):
        result = self.visualizer.generate_visualization(self.sample_data, 'scatter', 'x', 'y', 'Test Scatter Plot')
        self.assertIn('plot', result)
        self.assertEqual(result['type'], 'scatter')

    def test_generate_pie_chart(self):
        pie_data = pd.DataFrame({
            'category': ['A', 'B', 'C'],
            'value': [30, 50, 20]
        })
        result = self.visualizer.generate_visualization(pie_data, 'pie', 'category', 'value', 'Test Pie Chart')
        self.assertIn('plot', result)
        self.assertEqual(result['type'], 'pie')

    def test_suggest_visualization(self):
        suggestion = self.visualizer.suggest_visualization(self.sample_data)
        self.assertIn(suggestion, ['scatter', 'bar', 'line'])

    def test_unsupported_visualization_type(self):
        with self.assertRaises(ValueError):
            self.visualizer.generate_visualization(self.sample_data, 'unsupported', 'x', 'y')

if __name__ == '__main__':
    unittest.main()
