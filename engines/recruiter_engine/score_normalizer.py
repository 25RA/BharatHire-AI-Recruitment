"""
Score Normalization Engine
"""


class ScoreNormalizer:

    MIN_SCORE = 20
    MAX_SCORE = 85

    TARGET_MIN = 20
    TARGET_MAX = 100

    @staticmethod
    def normalize(score: float) -> float:

        score = max(
            ScoreNormalizer.MIN_SCORE,
            min(score, ScoreNormalizer.MAX_SCORE)
        )

        normalized = (

            (score - ScoreNormalizer.MIN_SCORE)

            /

            (
                ScoreNormalizer.MAX_SCORE
                -
                ScoreNormalizer.MIN_SCORE
            )

        ) * (

            ScoreNormalizer.TARGET_MAX
            -
            ScoreNormalizer.TARGET_MIN

        ) + ScoreNormalizer.TARGET_MIN

        return round(normalized, 2)