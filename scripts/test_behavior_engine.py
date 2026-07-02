import json

from preprocessing.parser import CandidateParser
from engines.candidate_engine.behavior_engine import BehaviorEngine

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as file:

    first = json.loads(next(file))

candidate = CandidateParser.parse(first)

features = BehaviorEngine.analyze(candidate)

print()

print("=" * 60)
print("BEHAVIOR INTELLIGENCE")
print("=" * 60)

for key, value in features.items():

    print(f"{key:35}: {value}")
    