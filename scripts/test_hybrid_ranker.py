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
from engines.recruiter_engine.industry_matcher import IndustryMatcher
from engines.recruiter_engine.assessment_matcher import AssessmentMatcher
from engines.recruiter_engine.risk_engine import RiskEngine
from engines.recruiter_engine.hybrid_ranker import HybridRanker


# ============================================================
# Load Candidate
# ============================================================

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

candidate = CandidateParser.parse(first)

intel = CandidateIntelligenceEngine.analyze(candidate)

# ============================================================
# Load JD
# ============================================================

text = JDLoader.load("job_description.docx")

jd = JDParser(text).parse()

requirements = RequirementEngine.extract(jd)

# ============================================================
# Individual Matchers
# ============================================================

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

industry = IndustryMatcher.match(
    intel["career"],
    requirements
)

assessment = AssessmentMatcher.match(
    candidate,
    requirements
)

risk = RiskEngine.score(
    candidate
)

# ============================================================
# Hybrid Ranking
# ============================================================

report = HybridRanker.rank(
    candidate_id=candidate.candidate_id,
    skill=skill,
    experience=experience,
    career=career,
    behavior=behavior,
    industry=industry,
    assessment=assessment,
    risk=risk
)

print("=" * 80)
print("BHARATHIRE HYBRID RANKING REPORT")
print("=" * 80)

pprint(report)

print("=" * 80)