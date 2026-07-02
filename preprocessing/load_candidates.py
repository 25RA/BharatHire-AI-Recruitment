"""
BharatHire Candidate Loader

Loads candidate JSONL data safely and returns a pandas DataFrame.
"""

from pathlib import Path
import json
from typing import Any

import pandas as pd
from loguru import logger


class CandidateLoader:
    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)

    def load(self) -> pd.DataFrame:

        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )

        candidates: list[dict[str, Any]] = []
        invalid_records = 0

        logger.info(f"Reading dataset from {self.dataset_path}")

        with self.dataset_path.open(
            "r",
            encoding="utf-8"
        ) as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    candidates.append(json.loads(line))

                except json.JSONDecodeError:

                    invalid_records += 1

                    logger.warning(
                        f"Invalid JSON at line {line_number}"
                    )

        df = pd.json_normalize(candidates)

        logger.success(f"Loaded {len(df)} candidates")
        logger.info(f"Invalid records : {invalid_records}")
        logger.info(f"Columns         : {len(df.columns)}")

        return df

    def save_processed(
        self,
        dataframe: pd.DataFrame,
        output_path: str
    ) -> None:

        output = Path(output_path)

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        dataframe.to_parquet(
            output,
            index=False
        )

        logger.success(
            f"Saved processed dataset to {output}"
        )


from evaluation.data_profiler import DataProfiler

if __name__ == "__main__":

    loader = CandidateLoader("candidates.jsonl")

    df = loader.load()

    loader.save_processed(
        df,
        "data/processed/candidates.parquet"
    )

    profiler = DataProfiler(df)

    profiler.profile()