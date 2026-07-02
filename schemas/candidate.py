"""
Candidate Domain Model

Represents one candidate inside BharatHire.
"""

from typing import Any

from pydantic import BaseModel


class Candidate(BaseModel):

    candidate_id: str

    profile: dict[str, Any]

    career_history: list[Any]

    education: list[Any]

    skills: list[Any]

    certifications: list[Any]

    languages: list[Any]

    redrob_signals: dict[str, Any]