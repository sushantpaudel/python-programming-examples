"""Lab 1 - Question 14: Filter students with marks greater than 75."""

import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"


def main():
    df = pd.read_csv(DATA_FILE)
    week1 = df[df["Week"] == 1][["Name", "Age", "Marks", "Category"]]

    print("All students (Week 1):")
    print(week1)
    print("\nStudents with marks > 75:")
    filtered = week1[week1["Marks"] > 75]
    print(filtered)


if __name__ == "__main__":
    main()
