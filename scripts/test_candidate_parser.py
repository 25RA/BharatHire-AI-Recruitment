import json

from preprocessing.parser import CandidateParser


with open(
    "candidates.jsonl",
    encoding="utf-8"
) as file:

    first_candidate = json.loads(next(file))

candidate = CandidateParser.parse(first_candidate)

print()

print("=" * 60)

print(candidate)

print("=" * 60)

print()

print("Candidate ID :", candidate.candidate_id)

print("Current Title :", candidate.profile.get("current_title"))

print("Experience :", candidate.profile.get("years_of_experience"))

print("Skills :", len(candidate.skills))

print("Career Records :", len(candidate.career_history))