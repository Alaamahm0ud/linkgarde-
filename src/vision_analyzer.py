import random

class VisionAnalyzer:
    async def analyze(self, image_data: bytes) -> dict:
        fake_logo_detected = random.choice([True, False])
        return {
            "vision_score": 0.9 if fake_logo_detected else 0.1,
            "details": "Fake logo detected" if fake_logo_detected else "Clean visuals",
        }
