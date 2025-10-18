from fastapi import FastAPI
from src.initializer import initializer
from src.rule_engine import RuleEngine
from src.result_cache import ResultCache
from src.threat_scoring import ThreatScoringService

app = FastAPI(title="LINKGARDE API")
engine = RuleEngine()
scorer = ThreatScoringService()

@app.on_event("startup")
async def startup_event():
    await initializer.initialize()

@app.post("/analyze")
async def analyze_link(data: dict):
    url = data.get("url")
    cache = ResultCache(initializer.redis)

    cached = await cache.get(url)
    if cached:
        return {"cached": True, "result": cached}

    rule_res = await engine.analyze(url)
    nlp_res = {"nlp_score": 0.2}  # placeholder
    total = await scorer.aggregate([rule_res, nlp_res])

    await cache.set(url, total)
    return {"cached": False, "result": total}

@app.get("/health")
async def health():
    return {"status": "OK"}
