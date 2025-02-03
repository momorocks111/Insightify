from .file_processing import FileProcessor

def __init__(self, model_manager):
    self.model_manager = model_manager
    self.nlp_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    self.intent_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
