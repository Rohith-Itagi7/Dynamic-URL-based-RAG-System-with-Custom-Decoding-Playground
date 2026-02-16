# rag/ingestion/text_cleaner.py

import re

class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        return text.strip()
