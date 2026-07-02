"""
Skill Matching Engine

Compares candidate skills with JD requirements.
"""

from typing import Any


class SkillMatcher:

    @staticmethod
    def match(
        candidate_skills: dict[str, Any],
        jd: dict[str, Any]
    ) -> dict[str, Any]:

        candidate = {
            skill.lower()
            for skill in candidate_skills.get(
                "unique_skills",
                []
            )
        }

        required = {
            skill.lower()
            for skill in jd.get(
                "required_skills",
                []
            )
        }

        preferred = {
            skill.lower()
            for skill in jd.get(
                "preferred_skills",
                []
            )
        }

        matched_required = sorted(
            candidate & required
        )

        missing_required = sorted(
            required - candidate
        )

        matched_preferred = sorted(
            candidate & preferred
        )

        required_score = (
            len(matched_required) / len(required)
            if required else 1.0
        )

        preferred_score = (
            len(matched_preferred) / len(preferred)
            if preferred else 1.0
        )

        overall_score = round(
            (
                required_score * 0.8
                + preferred_score * 0.2
            ) * 100,
            2
        )

        return {

            "required_match_score": round(
                required_score * 100,
                2
            ),

            "preferred_match_score": round(
                preferred_score * 100,
                2
            ),

            "overall_skill_score": overall_score,

            "matched_required": matched_required,

            "missing_required": missing_required,

            "matched_preferred": matched_preferred

        }