"""
Pipeline Evaluation
"""

import pandas as pd

from evaluation.analytics import AnalyticsEngine

FILE = "outputs/predictions/ranked_candidates.csv"

df = pd.read_csv(FILE)

AnalyticsEngine.generate(df)