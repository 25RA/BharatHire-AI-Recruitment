"""
JD Loader

Reads the job description from a DOCX file.
"""

from pathlib import Path
from docx import Document


class JDLoader:

    @staticmethod
    def load(path: str) -> str:

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(file)

        document = Document(file)

        text = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text.strip())

        return "\n".join(text)