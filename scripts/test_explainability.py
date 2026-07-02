import json
from pprint import pprint

from preprocessing.parser import CandidateParser

from engines.candidate_engine.candidate_intelligence import (
    CandidateIntelligenceEngine,
)

from engines.jd_engine.jd_loader import JDLoader
from engines.jd_engine.jd_parser import JDParser
from engines.jd_engine.requirement_engine import RequirementEngine

from engines.recruiter_engine.skill_matcher import SkillMatcher
from engines.recruiter_engine.experience_matcher import ExperienceMatcher
from engines.recruiter_engine.career_matcher import CareerMatcher
from engines.recruiter_engine.behavior_matcher import BehaviorMatcher
from engines.recruiter_engine.hybrid_ranker import HybridRanker

from engines.explainability_engine.explainability import (
    ExplainabilityEngine,
)

# -------------------------------------------------------
# Load Candidate
# -------------------------------------------------------

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

intel = CandidateIntelligenceEngine.analyze(candidate)

# -------------------------------------------------------
# Load JD
# -------------------------------------------------------

text = JDLoader.load("job_description.docx")

jd = JDParser(text).parse()

requirements = RequirementEngine.extract(jd)

# -------------------------------------------------------
# Matchers
# -------------------------------------------------------

skill = SkillMatcher.match(
    intel["skills"],
    requirements
)

experience = ExperienceMatcher.match(
    intel["career"],
    requirements
)

career = CareerMatcher.match(
    intel["career"],
    requirements
)

behavior = BehaviorMatcher.match(
    intel["behavior"],
    requirements
)

# -------------------------------------------------------
# Ranking
# -------------------------------------------------------

ranking = HybridRanker.rank(
    candidate.candidate_id,
    skill,
    experience,
    career,
    behavior
)

# -------------------------------------------------------
# Explainability
# -------------------------------------------------------

explanation = ExplainabilityEngine.explain(
    ranking=ranking,
    skill_report=skill,
    career_report=career,
    behavior_report=behavior,
)

print("=" * 80)
print("BHARATHIRE EXPLAINABILITY REPORT")
print("=" * 80)

pprint(explanation)

print("=" * 80)