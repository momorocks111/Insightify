import unittest
from unittest.mock import MagicMock
from app.services.query_processing import QueryProcessor
from app.services.model_management import ModelManager

class TestQueryProcessing(unittest.TestCase):
    def setUp(self):
        self.model_manager = MagicMock(spec=ModelManager)
        self.query_processor = QueryProcessor(self.model_manager)

    def test_process_query(self):
        # Mock the necessary methods
        self.query_processor.classify_query = MagicMock(return_value="POSITIVE")
        self.query_processor.route_query = MagicMock(return_value="gpt2_model")
        self.query_processor.execute_query = MagicMock(return_value="Mocked response")

        query = "What is the weather like today?"
        result = self.query_processor.process_query(query)

        self.assertEqual(result["classification"], "POSITIVE")
        self.assertEqual(result["model_used"], "gpt2_model")
        self.assertEqual(result["result"], "Mocked response")

    def test_classify_query(self):
        query = "I love this product!"
        classification = self.query_processor.classify_query(query)
        self.assertIn(classification, ["POSITIVE", "NEGATIVE"])

    def test_route_query(self):
        classification = "POSITIVE"
        model_name = self.query_processor.route_query(classification)
        self.assertEqual(model_name, "gpt2_model")

        classification = "NEGATIVE"
        model_name = self.query_processor.route_query(classification)
        self.assertEqual(model_name, "time_series_model")

if __name__ == '__main__':
    unittest.main()
