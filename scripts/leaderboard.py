"""
BharatHire Leaderboard Generator
"""

from pathlib import Path
import pandas as pd

INPUT = "outputs/predictions/ranked_candidates.csv"
OUTPUT = "outputs/leaderboard/top100.csv"

print("=" * 80)
print("Generating BharatHire Leaderboard")
print("=" * 80)

# Load predictions
df = pd.read_csv(INPUT)

# Sort by score
df = df.sort_values(
    by="overall_score",
    ascending=False
)

# Top 100
top100 = df.head(100)

# Create output directory
Path("outputs/leaderboard").mkdir(
    parents=True,
    exist_ok=True
)

# Save
top100.to_csv(
    OUTPUT,
    index=False
)

print()
print("=" * 80)
print("TOP 100 GENERATED")
print("=" * 80)

print(top100[
    [
        "candidate_id",
        "overall_score",
        "recommendation"
    ]
].head(20))

print()
print(f"Saved to : {OUTPUT}")