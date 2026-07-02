"""
Response Models
"""

from typing import List

from pydantic import BaseModel


class CandidateResponse(BaseModel):

    candidate_id: str

    overall_score: float

    recommendation: str

    confidence: float


class RankingResponse(BaseModel):

    total_candidates: int

    candidates: List[CandidateResponse]