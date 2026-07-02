"""
BharatHire Explainability Engine
"""


class ExplainabilityEngine:

    @staticmethod
    def explain(
        ranking: dict,
        skill_report: dict,
        career_report: dict,
        behavior_report: dict
    ):

        strengths = []
        concerns = []

        # ==================================================
        # Strength Analysis
        # ==================================================

        if ranking["skill_score"] >= 70:
            strengths.append("Excellent technical skill match")

        elif ranking["skill_score"] >= 50:
            strengths.append("Good technical skill match")

        else:
            concerns.append("Missing important required skills")

        # ==================================================
        # Experience Analysis
        # ==================================================

        if ranking["experience_score"] >= 90:
            strengths.append("Experience perfectly matches the JD")

        elif ranking["experience_score"] >= 75:
            strengths.append("Relevant experience")

        else:
            concerns.append("Experience below preferred range")

        # ==================================================
        # Career Analysis
        # ==================================================

        if career_report["career_score"] >= 85:
            strengths.append("Stable career progression")

        else:
            concerns.append("Career progression needs review")

        # ==================================================
        # Behavioral Analysis
        # ==================================================

        if behavior_report["behavior_score"] >= 75:
            strengths.append("Excellent recruiter engagement")

        elif behavior_report["behavior_score"] >= 60:
            strengths.append("Positive recruiter engagement")

        else:
            concerns.append("Behavioral profile could be stronger")

        # ==================================================
        # Recommendation
        # ==================================================

        score = ranking["overall_score"]

        if score >= 95:
            recommendation = "Elite Match"

        elif score >= 85:
            recommendation = "Strong Shortlist"

        elif score >= 70:
            recommendation = "Shortlist"

        elif score >= 55:
            recommendation = "Needs Manual Review"

        else:
            recommendation = "Not Recommended"

        # ==================================================
        # Confidence Score
        # ==================================================

        confidence = round(

            (

                ranking["skill_score"]

                + ranking["experience_score"]

                + ranking["career_score"]

                + ranking["behavior_score"]

                + ranking["industry_score"]

                + ranking["assessment_score"]

            ) / 6,

            2

        )

        # ==================================================
        # Dashboard Breakdown
        # ==================================================

        technical_fit = round(

            (

                ranking["skill_score"]

                + ranking["assessment_score"]

            ) / 2,

            2

        )

        experience_fit = round(

            (

                ranking["experience_score"]

                + ranking["career_score"]

            ) / 2,

            2

        )

        behavior_fit = round(

            (

                ranking["behavior_score"]

                + ranking["industry_score"]

            ) / 2,

            2

        )

        risk_score = ranking["risk_penalty"]

        # ==================================================
        # Final Report
        # ==================================================

        return {

            "overall_score": ranking["overall_score"],

            "confidence": confidence,

            "technical_fit": technical_fit,

            "experience_fit": experience_fit,

            "behavior_fit": behavior_fit,

            "risk_score": risk_score,

            "recommendation": recommendation,

            "strengths": strengths,

            "concerns": concerns

        }