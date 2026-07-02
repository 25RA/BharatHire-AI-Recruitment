import json
from pprint import pprint

from preprocessing.parser import CandidateParser
from engines.recruiter_engine.risk_engine import RiskEngine

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

report = RiskEngine.score(candidate)

print("=" * 60)
print("RISK REPORT")
print("=" * 60)

pprint(report)