import json

from preprocessing.parser import CandidateParser
from engines.candidate_engine.career_engine import CareerEngine

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as file:

    first = json.loads(next(file))

candidate = CandidateParser.parse(first)

career = CareerEngine.analyze(candidate)

print()

print("=" * 60)

print("CAREER INTELLIGENCE")

print("=" * 60)

for key, value in career.items():

    print(f"{key:35}: {value}")
    