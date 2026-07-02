import json

from preprocessing.parser import CandidateParser
from engines.candidate_engine.skill_engine import SkillEngine

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as file:

    first = json.loads(next(file))

candidate = CandidateParser.parse(first)

features = SkillEngine.analyze(candidate)

print()

print("=" * 60)
print("SKILL INTELLIGENCE")
print("=" * 60)

for key, value in features.items():

    print(f"{key:30}: {value}")