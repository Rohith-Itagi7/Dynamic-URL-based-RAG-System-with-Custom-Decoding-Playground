# generation/generation_engine.py

from generation.model_loader import ModelLoader
from generation.prompt_builder import PromptBuilder
from generation.decoding.decoding_router import decode


class GenerationEngine:

    def __init__(self):
        self.model, self.tokenizer = ModelLoader.load()

    def generate(self, context, query, params):
        prompt = PromptBuilder.build(context, query)

        inputs = self.tokenizer(prompt, return_tensors="pt")

        output_ids = decode(self.model, self.tokenizer, prompt, params)

        # 🔥 Slice only newly generated tokens
        generated_ids = output_ids[0][inputs["input_ids"].shape[1]:]

        answer = self.tokenizer.decode(generated_ids, skip_special_tokens=True)

        return answer.strip()
