"""
Skill Intelligence Engine v2
"""

from typing import Any


AI_SKILLS = {
    "Machine Learning",
    "Deep Learning",
    "LLMs",
    "LLM",
    "NLP",
    "Computer Vision",
    "PyTorch",
    "TensorFlow",
    "scikit-learn",
}

LLM_SKILLS = {
    "Prompt Engineering",
    "Fine-tuning LLMs",
    "LoRA",
    "QLoRA",
    "PEFT",
    "RAG",
    "LangChain",
    "LlamaIndex",
}

VECTOR_DB_SKILLS = {
    "FAISS",
    "Milvus",
    "Pinecone",
    "Qdrant",
    "Weaviate",
    "pgvector",
}

MLOPS_SKILLS = {
    "MLflow",
    "Kubeflow",
    "BentoML",
    "Weights & Biases",
}

BACKEND_SKILLS = {
    "Python",
    "Flask",
    "FastAPI",
    "SQL",
    "Kafka",
    "Spark",
}

# Master vocabulary used for inference
ALL_SKILLS = {
    "Python",
    "SQL",
    "FastAPI",
    "Flask",
    "Docker",
    "AWS",
    "Azure",
    "GCP",
    "LangChain",
    "LlamaIndex",
    "RAG",
    "FAISS",
    "Milvus",
    "Pinecone",
    "Qdrant",
    "Weaviate",
    "NLP",
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "LLM",
    "LLMs",
    "PyTorch",
    "TensorFlow",
    "Spark",
    "Kafka",
}


class SkillEngine:

    @staticmethod
    def analyze(candidate) -> dict[str, Any]:

        # --------------------------------------------------
        # 1. Structured skills from dataset
        # --------------------------------------------------

        skill_names = {
            skill.get("name", "").strip()
            for skill in candidate.skills
            if skill.get("name")
        }

        # --------------------------------------------------
        # 2. Collect searchable text
        # --------------------------------------------------

        profile = candidate.profile or {}

        summary = profile.get("summary", "")

        headline = profile.get("headline", "")

        current_title = profile.get("current_title", "")

        descriptions = " ".join(
            job.get("description", "")
            for job in candidate.career_history
        )

        searchable_text = (
            summary
            + " "
            + headline
            + " "
            + current_title
            + " "
            + descriptions
        ).lower()

        # --------------------------------------------------
        # 3. Infer skills from text
        # --------------------------------------------------

        inferred = set()

        for skill in ALL_SKILLS:

            if skill.lower() in searchable_text:

                inferred.add(skill)

        # Merge explicit + inferred skills
        skill_names.update(inferred)

        # --------------------------------------------------
        # 4. Return intelligence
        # --------------------------------------------------

        return {

            "total_skills": len(skill_names),

            "ai_skill_count":
                len(skill_names & AI_SKILLS),

            "llm_skill_count":
                len(skill_names & LLM_SKILLS),

            "vector_db_skill_count":
                len(skill_names & VECTOR_DB_SKILLS),

            "mlops_skill_count":
                len(skill_names & MLOPS_SKILLS),

            "backend_skill_count":
                len(skill_names & BACKEND_SKILLS),

            "unique_skills":
                sorted(skill_names)

        }