"""
Pipeline Service
"""

import subprocess
import sys
import pandas as pd


class PipelineService:

    FILE = "outputs/predictions/ranked_candidates.csv"

    @staticmethod
    def leaderboard(limit: int = 100):

        df = pd.read_csv(PipelineService.FILE)

        columns = [

            "candidate_id",

            "overall_score",

            "confidence",

            "recommendation"

        ]

        return (

            df

            .sort_values(

                "overall_score",

                ascending=False

            )[columns]

            .head(limit)

            .to_dict(orient="records")

        )

    @staticmethod
    def run_pipeline():

        subprocess.run(

            [

                sys.executable,

                "-m",

                "scripts.run_pipeline"

            ],

            check=True

        )

        return {

            "status": "success",

            "message": "Ranking completed successfully."

        }