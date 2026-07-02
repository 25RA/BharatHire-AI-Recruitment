import json
from pprint import pprint

from preprocessing.parser import CandidateParser

from engines.candidate_engine.career_engine import CareerEngine

from engines.recruiter_engine.career_matcher import (
    CareerMatcher
)

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as f:

    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

career = CareerEngine.analyze(candidate)

report = CareerMatcher.match(
    career,
    {}
)

print("=" * 70)
print("CAREER MATCH REPORT")
print("=" * 70)

pprint(report)