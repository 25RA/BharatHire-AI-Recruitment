"""
JD Intelligence Parser

Extracts structured information from a Job Description.
"""

import re


class JDParser:

    def __init__(self, text: str):
        self.text = text

    def extract_experience(self):
        patterns = [
            r'(\d+)\s*[-–—to]+\s*(\d+)\s*years',
            r'(\d+)\+\s*years',
            r'minimum\s*(\d+)\s*years',
            r'(\d+)\s*years'
        ]
        for pattern in patterns:
            match = re.search(
                pattern,
                self.text,
                flags=re.IGNORECASE
            )
            if match:
                if len(match.groups()) == 2:
                    return {
                        "minimum": int(match.group(1)),
                        "maximum": int(match.group(2))
                    }
                return {
                    "minimum": int(match.group(1)),
                    "maximum": None
                }
        return {
            "minimum": None,
            "maximum": None
        }

    def extract_education(self):

        education_keywords = [
            "B.Tech",
            "Bachelor",
            "Master",
            "M.Tech",
            "Computer Science",
            "Engineering",
            "Degree"
        ]

        found = []

        text = self.text.lower()

        for item in education_keywords:

            if item.lower() in text:

                found.append(item)

        return sorted(found)

    def extract_keywords(self):

        keywords = [

            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Computer Vision",

            "LLM",
            "LLMs",
            "LangChain",
            "LlamaIndex",
            "Prompt Engineering",
            "RAG",

            "FAISS",
            "Milvus",
            "Pinecone",
            "Qdrant",
            "Weaviate",

            "FastAPI",
            "Flask",

            "TensorFlow",
            "PyTorch",
            "SQL",
            "Docker",
            "AWS",
            "Azure",
            "GCP"

        ]

        found = []

        text = self.text.lower()

        for keyword in keywords:

            if keyword.lower() in text:

                found.append(keyword)

        return sorted(found)

    def parse(self):

        return {

            "experience": self.extract_experience(),

            "education": self.extract_education(),

            "keywords": self.extract_keywords(),

            "raw_text": self.text

        }