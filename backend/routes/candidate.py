"""
Candidate API
"""

from fastapi import APIRouter, HTTPException

from backend.services.candidate_service import CandidateService

router = APIRouter()


@router.get("/candidate/{candidate_id}")

def get_candidate(candidate_id: str):

    candidate = CandidateService.get(candidate_id)

    if candidate is None:

        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    return candidate