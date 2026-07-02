"""
Candidate Intelligence Engine

Combines all intelligence engines into one recruiter-ready profile.
"""

from typing import Any

from engines.candidate_engine.career_engine import CareerEngine
from engines.candidate_engine.skill_engine import SkillEngine
from engines.candidate_engine.behavior_engine import BehaviorEngine


class CandidateIntelligenceEngine:

    @staticmethod
    def analyze(candidate) -> dict[str, Any]:

        career = CareerEngine.analyze(candidate)

        skills = SkillEngine.analyze(candidate)

        behavior = BehaviorEngine.analyze(candidate)

        return {

            "candidate_id": candidate.candidate_id,

            "career": career,

            "skills": skills,

            "behavior": behavior

        }