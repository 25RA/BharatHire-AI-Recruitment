"""
Hybrid Ranking Engine
"""
from engines.recruiter_engine.score_normalizer import ScoreNormalizer

from configs.scoring_config import (
    SKILL_WEIGHT,
    EXPERIENCE_WEIGHT,
    CAREER_WEIGHT,
    BEHAVIOR_WEIGHT,
    INDUSTRY_WEIGHT,
    ASSESSMENT_WEIGHT,
    RISK_WEIGHT,
)


class HybridRanker:

    @staticmethod
    def rank(
        candidate_id: str,
        skill: dict,
        experience: dict,
        career: dict,
        behavior: dict,
        industry: dict,
        assessment: dict,
        risk: dict,
    ) -> dict:

        skill_score = skill.get("overall_skill_score", 0)

        experience_score = experience.get("experience_score", 0)

        career_score = career.get("career_score", 0)

        behavior_score = behavior.get("behavior_score", 0)

        industry_score = industry.get("industry_score", 0)

        assessment_score = assessment.get("assessment_score", 0)

        risk_penalty = risk.get("risk_penalty", 0)

        overall = round(

            skill_score * SKILL_WEIGHT +

            experience_score * EXPERIENCE_WEIGHT +

            career_score * CAREER_WEIGHT +

            behavior_score * BEHAVIOR_WEIGHT +

            industry_score * INDUSTRY_WEIGHT +

            assessment_score * ASSESSMENT_WEIGHT -

            risk_penalty * RISK_WEIGHT,

            2

        )
        
        normalized_score = ScoreNormalizer.normalize(
        overall
)

        return {

            "candidate_id": candidate_id,
            
            "raw_score": overall,

            "overall_score": normalized_score,

            "skill_score": skill_score,

            "experience_score": experience_score,

            "career_score": career_score,

            "behavior_score": behavior_score,

            "industry_score": industry_score,

            "assessment_score": assessment_score,

            "risk_penalty": risk_penalty

        }