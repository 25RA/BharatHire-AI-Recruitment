from pathlib import Path
import pandas as pd


class DataProfiler:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def profile(self):
        print("\n" + "=" * 70)
        print("BHARATHIRE DATA PROFILE")
        print("=" * 70)

        print(f"Rows              : {len(self.df):,}")
        print(f"Columns           : {len(self.df.columns)}")
        print(f"Memory Usage      : {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

        print("\nColumn Types")
        print("-" * 70)
        print(self.df.dtypes.value_counts())

        print("\nMissing Values (%)")
        print("-" * 70)

        missing = (
            self.df.isnull()
            .mean()
            .mul(100)
            .sort_values(ascending=False)
        )

        print(missing.head(20))

        print("\nTop-Level Columns")
        print("-" * 70)

        for column in self.df.columns:
            print(column)

        print("\nNumeric Summary")
        print("-" * 70)
        print(self.df.describe())

        print("\nProfile Complete.")