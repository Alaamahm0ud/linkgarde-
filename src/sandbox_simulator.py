import random
import asyncio

class DynamicSandbox:
    async def analyze(self, url: str) -> dict:
        await asyncio.sleep(0.2)
        redirect = random.choice(["none", "malicious", "safe"])
        return {
            "sandbox_result": redirect,
            "behavior_score": 0.8 if redirect == "malicious" else 0.2,
        }
