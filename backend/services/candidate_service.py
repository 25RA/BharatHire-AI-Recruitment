"""
Candidate Service
"""

import numpy as np
import pandas as pd


class CandidateService:

    FILE = "outputs/predictions/ranked_candidates.csv"

    @staticmethod
    def get(candidate_id: str):

        df = pd.read_csv(CandidateService.FILE)

        row = df[df["candidate_id"] == candidate_id]

        if row.empty:
            return None

        record = (
            row.iloc[0]
            .replace([np.inf, -np.inf], None)
            .where(pd.notnull(row.iloc[0]), None)
        )

        return record.to_dict()