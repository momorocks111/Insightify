import logging
from typing import Dict, Any
from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
from app.models.specialized_models import TimeSeriesModel, ImageClassificationModel

logger = logging.getLogger(__name__)

class QueryProcessor:
    def __init__(self, model_manager):
        self.model_manager = model_manager
        self.nlp_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
        self.intent_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def process_query(self, query: str) -> Dict[str, Any]:
        logger.info(f"Processing query: {query}")
        
        intent = self.classify_intent(query)
        model_name = self.route_query(intent)
        model = self.model_manager.get_model(model_name)
        result = self.execute_query(model, query, intent)
        
        return {
            "intent": intent,
            "model_used": model_name,
            "result": result
        }

    def classify_intent(self, query: str) -> str:
        intents = ["time_series_analysis", "image_classification", "general_query"]
        results = self.intent_classifier(query, candidate_labels=intents, multi_label=False)
        return results['labels'][0]

    def route_query(self, intent: str) -> str:
        intent_to_model = {
            "time_series_analysis": "time_series_model",
            "image_classification": "image_classification_model",
            "general_query": "gpt2_model"
        }
        return intent_to_model.get(intent, "gpt2_model")

    def execute_query(self, model: Any, query: str, intent: str) -> Any:
        if isinstance(model, GPT2LMHeadModel):
            return self.execute_gpt2_query(model, query)
        elif isinstance(model, TimeSeriesModel):
            return self.execute_time_series_query(model, query)
        elif isinstance(model, ImageClassificationModel):
            return self.execute_image_classification_query(model, query)
        else:
            return "Query execution not implemented for this model type"

    def execute_gpt2_query(self, model: GPT2LMHeadModel, query: str) -> str:
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        input_ids = tokenizer.encode(query, return_tensors='pt')
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
        return tokenizer.decode(output[0], skip_special_tokens=True)

    def execute_time_series_query(self, model: TimeSeriesModel, query: str) -> str:
        return "Time series analysis result placeholder"

    def execute_image_classification_query(self, model: ImageClassificationModel, query: str) -> str:
        return "Image classification result placeholder"

