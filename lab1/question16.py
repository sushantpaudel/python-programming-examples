"""Lab 1 - Question 16: Group student data by category and find average marks."""

import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"


def main():
    df = pd.read_csv(DATA_FILE)
    avg_by_category = df.groupby("Category")["Marks"].mean().round(2)

    print("Average marks by category:")
    print(avg_by_category)


if __name__ == "__main__":
    main()
