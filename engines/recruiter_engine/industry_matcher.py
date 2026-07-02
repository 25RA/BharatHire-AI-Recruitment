"""
Industry Matching Engine
"""

from typing import Any


class IndustryMatcher:

    INDUSTRY_SIMILARITY = {

        "Software Product": {
            "IT Services": 85,
            "SaaS": 95,
            "HR Tech": 90,
            "Marketplace": 80,
        },

        "IT Services": {
            "Software Product": 85,
            "Consulting": 90,
            "SaaS": 75,
        },

        "HR Tech": {
            "Software Product": 90,
            "Recruitment": 95,
            "SaaS": 85,
        }

    }

    @staticmethod
    def match(
        career: dict[str, Any],
        requirements: dict[str, Any]
    ) -> dict:

        candidate = career.get(
            "current_industry",
            ""
        )

        preferred = requirements.get(
            "preferred_industries",
            []
        )

        if not preferred:

            score = 100

        else:

            score = 40

            for industry in preferred:

                if candidate.lower() == industry.lower():

                    score = 100

                    break

                similarity = (
                    IndustryMatcher.INDUSTRY_SIMILARITY
                    .get(industry, {})
                    .get(candidate)
                )

                if similarity:

                    score = max(score, similarity)

        return {

            "industry_score": score,

            "candidate_industry": candidate

        }