from schemas.candidate import Candidate


class CandidateParser:

    @staticmethod
    def parse(candidate_json: dict) -> Candidate:

        return Candidate(
            candidate_id=candidate_json.get("candidate_id"),
            profile=candidate_json.get("profile", {}),
            career_history=candidate_json.get("career_history", []),
            education=candidate_json.get("education", []),
            skills=candidate_json.get("skills", []),
            certifications=candidate_json.get("certifications", []),
            languages=candidate_json.get("languages", []),
            redrob_signals=candidate_json.get("redrob_signals", {})
        )