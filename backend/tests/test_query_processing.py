import unittest
from unittest.mock import MagicMock, patch
from app.services.query_processing import QueryProcessor
from app.services.model_management import ModelManager
from transformers import GPT2LMHeadModel
from app.models.specialized_models import TimeSeriesModel, ImageClassificationModel

class TestQueryProcessing(unittest.TestCase):
    def setUp(self):
        self.model_manager = MagicMock(spec=ModelManager)
        with patch('app.services.query_processing.pipeline') as mock_pipeline:
            self.query_processor = QueryProcessor(self.model_manager)
            mock_pipeline.assert_called()

    def test_process_query(self):
        query = "What is the weather forecast for tomorrow?"
        self.query_processor.classify_intent = MagicMock(return_value="general_query")
        self.query_processor.route_query = MagicMock(return_value="gpt2_model")
        self.query_processor.execute_query = MagicMock(return_value="Sample response")
        
        result = self.query_processor.process_query(query)
        self.assertIn("intent", result)
        self.assertIn("model_used", result)
        self.assertIn("result", result)

    def test_classify_intent(self):
        query = "Predict stock prices for next week"
        mock_result = {'labels': ['time_series_analysis', 'image_classification', 'general_query']}
        self.query_processor.intent_classifier = MagicMock(return_value=mock_result)
        
        intent = self.query_processor.classify_intent(query)
        self.assertIn(intent, ["time_series_analysis", "image_classification", "general_query"])

    def test_route_query(self):
        intent = "time_series_analysis"
        model_name = self.query_processor.route_query(intent)
        self.assertEqual(model_name, "time_series_model")

    def test_execute_query_gpt2(self):
        mock_model = MagicMock(spec=GPT2LMHeadModel)
        query = "Tell me a joke"
        result = self.query_processor.execute_query(mock_model, query, "general_query")
        self.assertIsInstance(result, str)

    def test_execute_query_time_series(self):
        mock_model = MagicMock(spec=TimeSeriesModel)
        query = "Forecast sales for next month"
        result = self.query_processor.execute_query(mock_model, query, "time_series_analysis")
        self.assertIsInstance(result, str)

    def test_execute_query_image_classification(self):
        mock_model = MagicMock(spec=ImageClassificationModel)
        query = "What's in this image?"
        result = self.query_processor.execute_query(mock_model, query, "image_classification")
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
