"""
Behavior Matching Engine
"""

from typing import Any


class BehaviorMatcher:

    @staticmethod
    def match(
        behavior: dict[str, Any],
        requirements: dict[str, Any]
    ) -> dict[str, Any]:

        score = 0

        # Open to work
        if behavior.get("open_to_work"):
            score += 20

        # Hiring readiness
        readiness = behavior.get(
            "hiring_readiness_score",
            0
        )

        score += readiness * 0.4

        # Recruiter response
        response = behavior.get(
            "recruiter_response_rate",
            0
        )

        score += response * 20

        # Interview completion
        interview = behavior.get(
            "interview_completion_rate",
            0
        )

        score += interview * 10

        # Offer acceptance
        offer = behavior.get(
            "offer_acceptance_rate",
            0
        )

        score += offer * 10

        score = round(min(score, 100), 2)

        return {

            "behavior_score": score,

            "open_to_work":
                behavior.get("open_to_work"),

            "hiring_readiness":
                readiness,

            "recruiter_response":
                response

        }