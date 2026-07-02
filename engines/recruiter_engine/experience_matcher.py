"""
Experience Matching Engine
"""

from typing import Any


class ExperienceMatcher:

    @staticmethod
    def match(
        candidate_career: dict[str, Any],
        requirements: dict[str, Any]
    ) -> dict[str, Any]:

        candidate_exp = candidate_career.get(
            "total_experience_years",
            0
        )

        minimum = requirements.get(
            "minimum_experience"
        )

        maximum = requirements.get(
            "maximum_experience"
        )

        if minimum is None:
            score = 100.0

        elif candidate_exp < minimum:

            score = max(
                0,
                round(candidate_exp / minimum * 100, 2)
            )

        elif maximum is not None and candidate_exp > maximum:

            score = max(
                50,
                round(
                    100 - (candidate_exp - maximum) * 5,
                    2
                )
            )

        else:

            score = 100.0

        return {

            "candidate_experience": candidate_exp,

            "minimum_required": minimum,

            "maximum_required": maximum,

            "experience_score": score

        }