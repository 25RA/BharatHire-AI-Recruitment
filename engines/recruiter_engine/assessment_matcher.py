"""
Assessment Matching Engine
"""

from typing import Any


class AssessmentMatcher:

    @staticmethod
    def match(candidate, requirements: dict[str, Any]) -> dict:

        signals = candidate.redrob_signals

        assessments = signals.get(
            "skill_assessment_scores",
            {}
        )

        required = requirements.get(
            "required_skills",
            []
        )

        # ------------------------------------------
        # Case-insensitive lookup
        # ------------------------------------------

        assessment_lookup = {
            key.strip().lower(): value
            for key, value in assessments.items()
        }

        # ------------------------------------------
        # Skill aliases
        # ------------------------------------------

        aliases = {

            "llm": [
                "llms",
                "fine-tuning llms",
                "prompt engineering",
            ],

            "llms": [
                "llm",
                "fine-tuning llms",
                "prompt engineering",
            ],

            "machine learning": [
                "ml",
                "deep learning",
            ],
            
            "deep learning": [
                "machine learning",
            ],
            
            "computer vision": [
                "cv",
                "image classification",
                "object detection",
                "opencv",
                "yolo",
            ],

            "retrieval": [
                "semantic search",
                "information retrieval",
                "vector search",
                "bm25",
            ],

            "ranking": [
                "learning to rank",
            ],

            "vector database": [
                "milvus",
                "pinecone",
                "faiss",
                "qdrant",
                "weaviate",
            ],

            "nlp": [
                "text processing",
                "language models",
            ]
        }

        matched_scores = []

        matched_skills = []

        # ------------------------------------------
        # Matching
        # ------------------------------------------

        for skill in required:

            skill_lower = skill.lower()

            # Exact match
            if skill_lower in assessment_lookup:

                matched_scores.append(
                    assessment_lookup[skill_lower]
                )

                matched_skills.append(skill)

                continue

            # Alias match
            for alias in aliases.get(skill_lower, []):

                if alias in assessment_lookup:

                    matched_scores.append(
                        assessment_lookup[alias]
                    )

                    matched_skills.append(skill)

                    break

        # ------------------------------------------
        # Score
        # ------------------------------------------

        average = (
            sum(matched_scores) / len(matched_scores)
            if matched_scores else 0
        )

        return {

            "assessment_score": round(
                average,
                2
            ),

            "matched_assessments":
                len(matched_scores),

            "matched_skills":
                matched_skills

        }