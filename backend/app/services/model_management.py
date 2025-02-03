import joblib
from typing import Dict, Any
import logging
from pathlib import Path
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sklearn.base import BaseEstimator
import torch
from app.services.training_pipeline import TrainingPipeline

logger = logging.getLogger(__name__)

class ModelRegistry:
    def __init__(self, models_dir: str = 'models'):
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(exist_ok=True)
        self.models: Dict[str, Any] = {}

    def add_model(self, name: str, model: Any, metadata: Dict[str, Any] = None):
        logger.info(f"Adding model: {name}")
        self.models[name] = {
            'model': model,
            'metadata': metadata or {}
        }
        self._save_model(name)

    def get_model(self, name: str) -> Any:
        logger.info(f"Retrieving model: {name}")
        if name not in self.models:
            self._load_model(name)
        return self.models[name]['model']

    def get_metadata(self, name: str) -> Dict[str, Any]:
        if name not in self.models:
            self._load_model(name)
        return self.models[name]['metadata']

    def list_models(self) -> Dict[str, Dict[str, Any]]:
        return {name: self.get_metadata(name) for name in self.models}

    def _save_model(self, name: str):
        model_path = self.models_dir / f"{name}.joblib"
        joblib.dump(self.models[name], model_path)
        logger.info(f"Model {name} saved to {model_path}")

    def _load_model(self, name: str):
        model_path = self.models_dir / f"{name}.joblib"
        if not model_path.exists():
            raise ValueError(f"Model {name} not found")
        self.models[name] = joblib.load(model_path)
        logger.info(f"Model {name} loaded from {model_path}")

class ModelManager:
    def __init__(self):
        self.registry = ModelRegistry()

    def train_and_register_model(self, name: str, model_type: str, data: Any, **kwargs):
        logger.info(f"Training model: {name}")
        pipeline = TrainingPipeline(model_type)
        prepared_data = pipeline.prepare_data(data)
        pipeline.train(prepared_data, **kwargs)
        
        metadata = {
            'type': model_type,
            'training_data_shape': data.shape if hasattr(data, 'shape') else None,
            **kwargs
        }
        self.registry.add_model(name, pipeline.model, metadata)
        
        # Save the model
        model_path = self.registry.models_dir / f"{name}_model.pt"
        pipeline.save_model(str(model_path))

    def _train_gpt2(self, data, **kwargs):
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        # Implement fine-tuning logic here
        return model

    def _train_time_series(self, data, **kwargs):
        # Placeholder for time series model training logic
        model = BaseEstimator()
        return model

    def _train_image_classification(self, data, **kwargs):
        # Placeholder for image classification model training logic
        model = BaseEstimator()
        return model

    def get_model(self, name: str):
        model_data = self.registry.get_model(name)
        model_type = model_data['metadata']['type']
        pipeline = TrainingPipeline(model_type)
        model_path = self.registry.models_dir / f"{name}_model.pt"
        pipeline.load_model(str(model_path))
        return pipeline.model

    def list_models(self):
        return self.registry.list_models()