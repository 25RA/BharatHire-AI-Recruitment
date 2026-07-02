import json
from pprint import pprint

from preprocessing.parser import CandidateParser
from engines.candidate_engine.career_engine import CareerEngine
from engines.recruiter_engine.industry_matcher import IndustryMatcher

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

career = CareerEngine.analyze(candidate)

requirements = {
    "preferred_industries": [
        "IT Services",
        "Software Product"
    ]
}

report = IndustryMatcher.match(
    career,
    requirements
)

print("=" * 60)
print("INDUSTRY MATCH REPORT")
print("=" * 60)

pprint(report)