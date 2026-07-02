"""
Career Matching Engine

Scores career progression, stability and industry alignment.
"""

from typing import Any


class CareerMatcher:

    @staticmethod
    def match(
        career: dict[str, Any],
        requirements: dict[str, Any]
    ) -> dict[str, Any]:

        score = 0

        # Stable career
        avg_tenure = career.get(
            "average_tenure_months",
            0
        )

        if avg_tenure >= 24:
            score += 30

        elif avg_tenure >= 12:
            score += 20

        else:
            score += 10

        # Experience with multiple companies
        companies = career.get(
            "companies_worked",
            0
        )

        if 2 <= companies <= 5:
            score += 20

        elif companies == 1:
            score += 15

        else:
            score += 10

        # Current role available
        if career.get("current_role"):
            score += 20

        # Current industry available
        if career.get("current_industry"):
            score += 20

        # Job hopping score
        hop = career.get(
            "job_hopping_score",
            0
        )

        if hop >= 2:
            score += 10

        return {

            "career_score": round(score, 2),

            "average_tenure":
                avg_tenure,

            "companies":
                companies,

            "current_role":
                career.get("current_role"),

            "industry":
                career.get("current_industry")
        }