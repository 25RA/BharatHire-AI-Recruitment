"""
Behavior Intelligence Engine
"""

from typing import Any


class BehaviorEngine:

    @staticmethod
    def analyze(candidate) -> dict[str, Any]:

        signal = candidate.redrob_signals

        profile_score = signal.get(
            "profile_completeness_score",
            0
        )

        recruiter_response = signal.get(
            "recruiter_response_rate",
            0
        )

        github = signal.get(
            "github_activity_score",
            0
        )

        interview = signal.get(
            "interview_completion_rate",
            0
        )

        offer = signal.get(
            "offer_acceptance_rate",
            0
        )

        open_to_work = signal.get(
            "open_to_work_flag",
            False
        )

        return {

            "profile_score": profile_score,

            "github_score": github,

            "recruiter_response_rate": recruiter_response,

            "interview_completion_rate": interview,

            "offer_acceptance_rate": offer,

            "open_to_work": open_to_work,

            "hiring_readiness_score": round(
                (
                    profile_score
                    + github * 10
                    + recruiter_response * 100
                    + interview * 100
                    + offer * 100
                ) / 5,
                2
            )

        }