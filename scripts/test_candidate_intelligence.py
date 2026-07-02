import json
from pprint import pprint

from preprocessing.parser import CandidateParser
from engines.candidate_engine.candidate_intelligence import (
    CandidateIntelligenceEngine,
)

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as file:

    first = json.loads(next(file))

candidate = CandidateParser.parse(first)

report = CandidateIntelligenceEngine.analyze(candidate)

print()
print("=" * 80)
print("BHARATHIRE CANDIDATE INTELLIGENCE REPORT")
print("=" * 80)

pprint(report, sort_dicts=False)

print("=" * 80)