"""Lab 1 - Question 21: Pie chart showing percentage distribution of grades."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def marks_to_grade(mark):
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def main():
    df = pd.read_csv(DATA_FILE)
    df["Grade"] = df["Marks"].apply(marks_to_grade)
    grade_counts = df["Grade"].value_counts().sort_index()

    print("Grade distribution (count):")
    print(grade_counts)
    print("\nPercentage distribution:")
    print((grade_counts / grade_counts.sum() * 100).round(2))

    plt.figure(figsize=(7, 7))
    plt.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#4caf50", "#8bc34a", "#ffc107", "#ff9800", "#f44336"],
    )
    plt.title("Percentage distribution of grades")
    plt.tight_layout()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_file = OUTPUT_DIR / "question21_pie_chart.png"
    plt.savefig(out_file)
    plt.close()
    print(f"\nPie chart saved to: {out_file}")


if __name__ == "__main__":
    main()
