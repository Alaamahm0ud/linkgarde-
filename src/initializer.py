import asyncio
import redis.asyncio as aioredis
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from config.settings import app, redis as redis_cfg, models

class ComponentInitializer:
    def __init__(self):
        self.redis = None
        self.tokenizer = None
        self.nlp_model = None

    async def initialize(self):
        print(f"🚀 Initializing {app['name']} components...")

        # Redis Connection
        self.redis = aioredis.from_url(
            f"redis://{redis_cfg['host']}:{redis_cfg['port']}/{redis_cfg['db']}"
        )

        # Load NLP Model
        self.tokenizer = AutoTokenizer.from_pretrained(models["nlp_model"])
        self.nlp_model = AutoModelForSequenceClassification.from_pretrained(
            models["nlp_model"]
        )

        print("✅ Initialization complete.")
        return self

initializer = ComponentInitializer()
