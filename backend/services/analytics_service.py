"""
Analytics Service
"""

import json


class AnalyticsService:

    FILE = "outputs/analytics/dashboard_metrics.json"

    @staticmethod
    def get():

        with open(

            AnalyticsService.FILE,

            encoding="utf-8"

        ) as f:

            return json.load(f)