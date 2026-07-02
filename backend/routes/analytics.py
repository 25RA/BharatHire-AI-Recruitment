"""
Analytics API
"""

from fastapi import APIRouter

from backend.services.analytics_service import AnalyticsService


router = APIRouter()


@router.get("/analytics")

def analytics():

    return AnalyticsService.get()