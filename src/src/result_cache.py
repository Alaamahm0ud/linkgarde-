import hashlib
import json

class ResultCache:
    def __init__(self, redis_client):
        self.redis = redis_client

    def _make_key(self, url: str) -> str:
        return f"linkgarde:{hashlib.sha256(url.encode()).hexdigest()}"

    async def get(self, url: str):
        data = await self.redis.get(self._make_key(url))
        return json.loads(data) if data else None

    async def set(self, url: str, result: dict, ttl=3600):
        await self.redis.set(self._make_key(url), json.dumps(result), ex=ttl)
