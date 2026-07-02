"""
BharatHire Full Ranking Pipeline
Processes every candidate and generates ranked_candidates.csv
"""

import csv
import json
import time
from pathlib import Path

from tqdm import tqdm

from preprocessing.parser import CandidateParser

from engines.candidate_engine.candidate_intelligence import (
    CandidateIntelligenceEngine
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

from engines.explainability_engine.explainability import (
    ExplainabilityEngine
)

# ==========================================================
# Configuration
# ==========================================================

DATASET = "candidates.jsonl"

OUTPUT = "outputs/predictions/ranked_candidates.csv"

JD_FILE = "job_description.docx"

# ==========================================================
# Load JD only once
# ==========================================================

print("=" * 80)
print("Loading Job Description...")
print("=" * 80)

jd_text = JDLoader.load(JD_FILE)

jd = JDParser(jd_text).parse()

requirements = RequirementEngine.extract(jd)

print("JD Loaded Successfully\n")

# ==========================================================
# CSV Header
# ==========================================================

header = [

    "candidate_id",

    "overall_score",

    "raw_score",

    "skill_score",

    "experience_score",

    "career_score",

    "behavior_score",

    "industry_score",

    "assessment_score",

    "risk_penalty",

    "confidence",

    "technical_fit",

    "experience_fit",

    "behavior_fit",

    "risk_score",

    "recommendation",

    "strengths",

    "concerns"

]

Path("outputs/predictions").mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# Processing
# ==========================================================

processed = 0
failed = 0

start = time.time()

with open(
    OUTPUT,
    "w",
    newline="",
    encoding="utf-8"
) as outfile:

    writer = csv.writer(outfile)

    writer.writerow(header)

    with open(
        DATASET,
        encoding="utf-8"
    ) as infile:

        for line in tqdm(infile):

            try:

                raw = json.loads(line)

                candidate = CandidateParser.parse(raw)

                intelligence = CandidateIntelligenceEngine.analyze(
                    candidate
                )

                skill = SkillMatcher.match(
                    intelligence["skills"],
                    requirements
                )

                experience = ExperienceMatcher.match(
                    intelligence["career"],
                    requirements
                )

                career = CareerMatcher.match(
                    intelligence["career"],
                    requirements
                )

                behavior = BehaviorMatcher.match(
                    intelligence["behavior"],
                    requirements
                )

                industry = IndustryMatcher.match(
                    intelligence["career"],
                    requirements
                )

                assessment = AssessmentMatcher.match(
                    candidate,
                    requirements
                )

                risk = RiskEngine.score(
                    candidate
                )

                ranking = HybridRanker.rank(

                    candidate_id=candidate.candidate_id,

                    skill=skill,

                    experience=experience,

                    career=career,

                    behavior=behavior,

                    industry=industry,

                    assessment=assessment,

                    risk=risk

                )

                explanation = ExplainabilityEngine.explain(

                    ranking,

                    skill,

                    career,

                    behavior

                )

                writer.writerow([

                    ranking["candidate_id"],

                    ranking["overall_score"],

                    ranking["raw_score"],

                    ranking["skill_score"],

                    ranking["experience_score"],

                    ranking["career_score"],

                    ranking["behavior_score"],

                    ranking["industry_score"],

                    ranking["assessment_score"],

                    ranking["risk_penalty"],
                    
                    explanation["confidence"],

                    explanation["technical_fit"],

                    explanation["experience_fit"],

                    explanation["behavior_fit"],

                    explanation["risk_score"],

                    explanation["recommendation"],

                    "; ".join(
                        explanation["strengths"]
                    ),

                    "; ".join(
                        explanation["concerns"]
                    )

                ])

                processed += 1

            except Exception:

                failed += 1

elapsed = round(
    time.time() - start,
    2
)

print("\n")
print("=" * 80)
print("BHARATHIRE PIPELINE COMPLETED")
print("=" * 80)

print(f"Processed : {processed:,}")
print(f"Failed    : {failed:,}")
print(f"Time      : {elapsed} sec")
print(f"\nOutput Saved : {OUTPUT}")