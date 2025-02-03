import unittest
from app.services.model_management import ModelManager
import pandas as pd
import torch

class TestModelManagement(unittest.TestCase):
    def setUp(self):
        self.model_manager = ModelManager()

    def test_train_and_register_gpt2(self):
        # Mock data for GPT-2 training
        data = ["This is a test sentence.", "Another test sentence."]
        self.model_manager.train_and_register_model("test_gpt2", "gpt2", data)
        models = self.model_manager.list_models()
        self.assertIn("test_gpt2", models)
        self.assertEqual(models["test_gpt2"]["type"], "gpt2")

    def test_train_and_register_time_series(self):
        # Mock data for time series training
        data = pd.DataFrame({'date': pd.date_range(start='1/1/2020', periods=100),
                             'value': range(100)})
        self.model_manager.train_and_register_model("test_time_series", "time_series", data)
        models = self.model_manager.list_models()
        self.assertIn("test_time_series", models)
        self.assertEqual(models["test_time_series"]["type"], "time_series")

    def test_get_model(self):
        # Train and register a model
        data = ["Test data"]
        self.model_manager.train_and_register_model("test_model", "gpt2", data)
        
        # Retrieve the model
        model = self.model_manager.get_model("test_model")
        self.assertIsNotNone(model)
        self.assertTrue(isinstance(model, torch.nn.Module))

    def test_list_models(self):
        # Train and register multiple models
        self.model_manager.train_and_register_model("model1", "gpt2", ["Data1"])
        self.model_manager.train_and_register_model("model2", "time_series", pd.DataFrame())
        
        models = self.model_manager.list_models()
        self.assertIn("model1", models)
        self.assertIn("model2", models)
        self.assertEqual(len(models), 2)

if __name__ == '__main__':
    unittest.main()
