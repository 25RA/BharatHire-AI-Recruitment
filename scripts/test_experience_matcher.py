import json
from pprint import pprint

from preprocessing.parser import CandidateParser

from engines.candidate_engine.career_engine import CareerEngine

from engines.jd_engine.jd_loader import JDLoader
from engines.jd_engine.jd_parser import JDParser
from engines.jd_engine.requirement_engine import RequirementEngine

from engines.recruiter_engine.experience_matcher import ExperienceMatcher

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

career = CareerEngine.analyze(candidate)

text = JDLoader.load("job_description.docx")

jd = JDParser(text).parse()

requirements = RequirementEngine.extract(jd)

report = ExperienceMatcher.match(
    career,
    requirements
)

print("=" * 70)
print("EXPERIENCE MATCH REPORT")
print("=" * 70)

pprint(report)