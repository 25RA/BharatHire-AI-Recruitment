import json
from pprint import pprint

from preprocessing.parser import CandidateParser

from engines.candidate_engine.behavior_engine import BehaviorEngine

from engines.recruiter_engine.behavior_matcher import (
    BehaviorMatcher
)

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as f:

    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

behavior = BehaviorEngine.analyze(candidate)

report = BehaviorMatcher.match(
    behavior,
    {}
)

print("=" * 70)
print("BEHAVIOR MATCH REPORT")
print("=" * 70)

pprint(report)
