"""
Generate Competition Submission
"""

from pathlib import Path
import pandas as pd

INPUT = "outputs/leaderboard/top100.csv"

OUTPUT = "outputs/submissions/submission.csv"

df = pd.read_csv(INPUT)

submission = df[
    [
        "candidate_id",
        "overall_score"
    ]
]

Path("outputs/submissions").mkdir(
    parents=True,
    exist_ok=True
)

submission.to_csv(
    OUTPUT,
    index=False
)

print("=" * 80)
print("SUBMISSION GENERATED")
print("=" * 80)

print(submission.head(10))

print()

print(f"Saved : {OUTPUT}")