import json
from pprint import pprint

from preprocessing.parser import CandidateParser
from engines.candidate_engine.skill_engine import SkillEngine
from engines.jd_engine.jd_loader import JDLoader
from engines.jd_engine.jd_parser import JDParser
from engines.jd_engine.requirement_engine import RequirementEngine
from engines.recruiter_engine.skill_matcher import SkillMatcher

with open(
    "candidates.jsonl",
    encoding="utf-8"
) as file:

    first = json.loads(next(file))

candidate = CandidateParser.parse(first)

candidate_skills = SkillEngine.analyze(candidate)

text = JDLoader.load("job_description.docx")

jd = JDParser(text).parse()

requirements = RequirementEngine.extract(jd)

report = SkillMatcher.match(
    candidate_skills,
    requirements
)

print()
print("=" * 80)
print("SKILL MATCH REPORT")
print("=" * 80)

pprint(report, sort_dicts=False)