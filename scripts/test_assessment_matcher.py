import json
from pprint import pprint

from preprocessing.parser import CandidateParser
from engines.jd_engine.jd_loader import JDLoader
from engines.jd_engine.jd_parser import JDParser
from engines.jd_engine.requirement_engine import RequirementEngine

from engines.recruiter_engine.assessment_matcher import (
    AssessmentMatcher
)

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

text = JDLoader.load("job_description.docx")

jd = JDParser(text).parse()

requirements = RequirementEngine.extract(jd)

report = AssessmentMatcher.match(
    candidate,
    requirements
)

print("=" * 60)
print("ASSESSMENT MATCH REPORT")
print("=" * 60)

pprint(report)