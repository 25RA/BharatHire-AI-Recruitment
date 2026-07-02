"""
Requirement Engine

Converts parsed JD into structured recruiter requirements.
"""

from typing import Any


class RequirementEngine:

    @staticmethod
    def extract(jd: dict[str, Any]) -> dict[str, Any]:

        keywords = jd.get("keywords", [])

        experience = jd.get("experience", {})

        raw_text = jd.get("raw_text", "").lower()

        # ------------------------------------------------------
        # Dynamic Skill Classification
        # ------------------------------------------------------

        CRITICAL_SKILLS = {
            "Python",
            "RAG",
            "LangChain",
            "LLM",
            "LLMs",
            "FAISS",
            "Machine Learning",
            "Learning to Rank",
            "Ranking",
            "Retrieval",
            "Embeddings",
        }

        REQUIRED_SKILLS = []
        PREFERRED_SKILLS = []

        for skill in keywords:

            if skill in CRITICAL_SKILLS:
                REQUIRED_SKILLS.append(skill)
            else:
                PREFERRED_SKILLS.append(skill)

        # ------------------------------------------------------
        # Preferred Industries
        # ------------------------------------------------------

        preferred_industries = []

        if "product company" in raw_text:
            preferred_industries.append("Software Product")

        if "it services" in raw_text:
            preferred_industries.append("IT Services")

        if "hr-tech" in raw_text:
            preferred_industries.append("HR Tech")

        if "marketplace" in raw_text:
            preferred_industries.append("Marketplace")

        # ------------------------------------------------------
        # Preferred Locations
        # ------------------------------------------------------

        preferred_locations = []

        LOCATION_KEYWORDS = [
            "Pune",
            "Noida",
            "Hyderabad",
            "Mumbai",
            "Delhi NCR",
        ]

        for city in LOCATION_KEYWORDS:

            if city.lower() in raw_text:

                preferred_locations.append(city)

        # ------------------------------------------------------
        # Preferred Titles
        # ------------------------------------------------------

        preferred_titles = [

            "AI Engineer",

            "Machine Learning Engineer",

            "ML Engineer",

            "Data Scientist",

            "Search Engineer",

            "Recommendation Engineer",

            "NLP Engineer"

        ]

        # ------------------------------------------------------
        # Final Requirement Object
        # ------------------------------------------------------

        return {

            "required_skills": sorted(REQUIRED_SKILLS),

            "preferred_skills": sorted(PREFERRED_SKILLS),

            "preferred_industries": preferred_industries,

            "preferred_locations": preferred_locations,

            "preferred_titles": preferred_titles,

            "minimum_experience":
                experience.get("minimum"),

            "maximum_experience":
                experience.get("maximum")

        }