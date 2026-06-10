"""Lab 1 - Question 17: Read a CSV file using Pandas and display first 5 rows."""

import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"


def main():
    df = pd.read_csv(DATA_FILE)
    print(f"Reading: {DATA_FILE.name}\n")
    print("First 5 rows:")
    print(df.head())


if __name__ == "__main__":
    main()
