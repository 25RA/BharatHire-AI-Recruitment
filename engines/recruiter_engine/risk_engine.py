"""
Risk Engine
"""


class RiskEngine:

    @staticmethod
    def score(candidate) -> dict:

        signals = candidate.redrob_signals

        risk = 0

        notice = signals.get(
            "notice_period_days",
            0
        )

        if notice > 90:
            risk += 15

        if signals.get(
            "profile_completeness_score",
            100
        ) < 60:
            risk += 10

        if signals.get(
            "recruiter_response_rate",
            1
        ) < 0.2:
            risk += 10

        return {

            "risk_penalty": risk

        }