"""
Upload & Ranking API
"""

from fastapi import APIRouter

from backend.services.pipeline_service import PipelineService

router = APIRouter()


@router.post("/rank")
def run_ranking():
    """
    Run the BharatHire ranking pipeline.

    Returns:
        Ranking status and pipeline result.
    """
    return PipelineService.run_pipeline()