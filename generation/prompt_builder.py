class PromptBuilder:

    @staticmethod
    def build(context, query):
        return f"""
You are a professional summarization assistant.

Strict Instructions:
- Summarize only the provided context.
- Do not invent information.
- Do not change topic.
- Maximum 4 sentences.

Context:
{context}

Final Summary:
"""
