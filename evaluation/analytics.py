"""
BharatHire Analytics Engine
"""

import json
from pathlib import Path
from collections import Counter


class AnalyticsEngine:

    @staticmethod
    def generate(df):

        analytics = {}

        # ==================================================
        # Basic Statistics
        # ==================================================

        analytics["candidates_processed"] = int(len(df))

        analytics["average_score"] = round(
            float(df["overall_score"].mean()),
            2
        )

        analytics["highest_score"] = round(
            float(df["overall_score"].max()),
            2
        )

        analytics["lowest_score"] = round(
            float(df["overall_score"].min()),
            2
        )

        # ==================================================
        # Recommendation Distribution
        # ==================================================

        recommendation_counts = (
            df["recommendation"]
            .value_counts()
            .to_dict()
        )

        analytics["recommendations"] = recommendation_counts

        # ==================================================
        # Component Averages
        # ==================================================

        components = {}

        for column in [

            "skill_score",

            "experience_score",

            "career_score",

            "behavior_score",

            "industry_score",

            "assessment_score"

        ]:

            if column in df.columns:

                components[column] = round(
                    float(df[column].mean()),
                    2
                )

        analytics["component_scores"] = components

        # ==================================================
        # Confidence
        # ==================================================

        if "confidence" in df.columns:

            analytics["confidence"] = {

                "average": round(
                    float(df["confidence"].mean()),
                    2
                ),

                "maximum": round(
                    float(df["confidence"].max()),
                    2
                )

            }

        # ==================================================
        # Top 10 Candidates
        # ==================================================

        top10 = (

            df.sort_values(

                by="overall_score",

                ascending=False

            )[

                [

                    "candidate_id",

                    "overall_score",

                    "recommendation"

                ]

            ]

            .head(10)

            .to_dict(

                orient="records"

            )

        )

        analytics["top_candidates"] = top10

        # ==================================================
        # Strength Analysis
        # ==================================================

        strengths = Counter()

        if "strengths" in df.columns:

            for row in df["strengths"].fillna(""):

                for item in row.split(";"):

                    item = item.strip()

                    if item:

                        strengths[item] += 1

        analytics["top_strengths"] = dict(
            strengths.most_common(10)
        )

        # ==================================================
        # Concern Analysis
        # ==================================================

        concerns = Counter()

        if "concerns" in df.columns:

            for row in df["concerns"].fillna(""):

                for item in row.split(";"):

                    item = item.strip()

                    if item:

                        concerns[item] += 1

        analytics["top_concerns"] = dict(
            concerns.most_common(10)
        )

        # ==================================================
        # Save JSON
        # ==================================================

        Path(
            "outputs/analytics"
        ).mkdir(
            parents=True,
            exist_ok=True
        )

        with open(

            "outputs/analytics/dashboard_metrics.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                analytics,

                f,

                indent=4

            )

        # ==================================================
        # Terminal Output
        # ==================================================

        print("=" * 80)
        print("BHARATHIRE ANALYTICS")
        print("=" * 80)

        print()

        print(f"Candidates Processed : {analytics['candidates_processed']:,}")

        print(f"Average Score        : {analytics['average_score']}")

        print(f"Highest Score        : {analytics['highest_score']}")

        print(f"Lowest Score         : {analytics['lowest_score']}")

        print()

        print("=" * 40)
        print("RECOMMENDATION DISTRIBUTION")
        print("=" * 40)

        for k, v in analytics["recommendations"].items():

            print(f"{k:<25} : {v:,}")

        print()

        print("=" * 40)
        print("AVERAGE COMPONENT SCORES")
        print("=" * 40)

        for k, v in analytics["component_scores"].items():

            print(f"{k:<25}: {v}")

        print()

        if "confidence" in analytics:

            print("=" * 40)
            print("CONFIDENCE")
            print("=" * 40)

            print(
                f"Average Confidence : {analytics['confidence']['average']}"
            )

            print(
                f"Maximum Confidence : {analytics['confidence']['maximum']}"
            )

            print()

        print("=" * 40)
        print("TOP 10 CANDIDATES")
        print("=" * 40)

        for candidate in analytics["top_candidates"]:

            print(
                candidate["candidate_id"],
                "|",
                candidate["overall_score"],
                "|",
                candidate["recommendation"]
            )

        print()

        print("=" * 80)
        print("Analytics JSON Saved")
        print("outputs/analytics/dashboard_metrics.json")
        print("=" * 80)