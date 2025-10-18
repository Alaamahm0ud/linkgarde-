import random

class AttackerFingerprinting:
    async def analyze(self, url: str) -> dict:
        age_days = random.randint(1, 3000)
        score = 0.9 if age_days < 30 else 0.1
        return {
            "domain_age": age_days,
            "infra_score": score,
            "details": "Recently registered domain" if score > 0.7 else "Trusted domain",
        }
