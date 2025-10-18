import re

class RuleEngine:
    def __init__(self):
        self.suspicious_keywords = ["login", "verify", "account", "bank"]
        self.blacklisted_domains = ["phishy.io", "stealer.net", "fakeupdate.com"]

    async def analyze(self, url: str) -> dict:
        result = {"rule_score": 0, "alerts": []}

        for word in self.suspicious_keywords:
            if word in url.lower():
                result["alerts"].append(f"Keyword match: {word}")
                result["rule_score"] += 1

        for domain in self.blacklisted_domains:
            if domain in url:
                result["alerts"].append(f"Blacklisted domain: {domain}")
                result["rule_score"] += 3

        return result
