# generation/model_loader.py
from transformers import AutoTokenizer, AutoModelForCausalLM

class ModelLoader:
    _model = None
    _tokenizer = None

    @classmethod
    def load(cls):
        if cls._model is None:
            cls._tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
            cls._model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
        return cls._model, cls._tokenizer
