"""
Career Intelligence Engine

Transforms raw career history into recruiter-friendly features.
"""

from typing import Any


class CareerEngine:

    @staticmethod
    def analyze(candidate) -> dict[str, Any]:

        history = candidate.career_history

        if not history:
            return {
                "total_experience_years": 0,
                "companies_worked": 0,
                "average_tenure_months": 0,
                "longest_tenure_months": 0,
                "current_company_tenure_months": 0,
                "job_hopping_score": 0,
                "current_role": "",
                "current_industry": ""
            }

        tenures = [
            job.get("duration_months", 0)
            for job in history
        ]

        companies = len(history)

        average_tenure = sum(tenures) / companies

        longest = max(tenures)

        current = next(
            (
                job
                for job in history
                if job.get("is_current")
            ),
            history[0]
        )

        current_tenure = current.get(
            "duration_months",
            0
        )

        total_experience = (
            candidate.profile.get(
                "years_of_experience",
                0
            )
        )

        job_hopping = round(
            total_experience / companies,
            2
        )

        return {

            "total_experience_years": total_experience,

            "companies_worked": companies,

            "average_tenure_months": round(
                average_tenure,
                2
            ),

            "longest_tenure_months": longest,

            "current_company_tenure_months": current_tenure,

            "job_hopping_score": job_hopping,

            "current_role": candidate.profile.get(
                "current_title",
                ""
            ),

            "current_industry": candidate.profile.get(
                "current_industry",
                ""
            )
        }