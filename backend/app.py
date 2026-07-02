"""
BharatHire FastAPI Backend
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.analytics import router as analytics_router
from backend.routes.candidate import router as candidate_router
from backend.routes.ranking import router as ranking_router
from backend.routes.upload import router as upload_router

app = FastAPI(

    title="BharatHire API",

    version="1.0.0",

    description="AI Recruitment Platform"

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {

        "message": "Welcome to BharatHire",

        "status": "Running"

    }


# ==========================
# Register API Routes
# ==========================

app.include_router(analytics_router)

app.include_router(candidate_router)

app.include_router(upload_router)

app.include_router(ranking_router)