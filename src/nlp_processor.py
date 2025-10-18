import torch

class NLPProcessor:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    async def analyze(self, text: str) -> dict:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            score = torch.softmax(outputs.logits, dim=1)[0][1].item()

        return {
            "nlp_score": round(score, 3),
            "meaning": "phishing intent detected" if score > 0.7 else "normal text",
        }
