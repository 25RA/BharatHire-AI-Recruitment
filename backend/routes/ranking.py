"""
Leaderboard API
"""

from fastapi import APIRouter

from backend.services.pipeline_service import PipelineService


router = APIRouter()


@router.get("/leaderboard")

def leaderboard(limit: int = 100):

    return {

        "count": limit,

        "results": PipelineService.leaderboard(limit)

    }