"""Lab 1 - Question 19: Bar chart comparing marks of five students."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "data" / "students.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


def main():
    df = pd.read_csv(DATA_FILE)
    week1 = df[df["Week"] == 1].head(5)

    plt.figure(figsize=(8, 5))
    plt.bar(week1["Name"], week1["Marks"], color="steelblue")
    plt.title("Marks comparison — five students (Week 1)")
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.tight_layout()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_file = OUTPUT_DIR / "question19_bar_chart.png"
    plt.savefig(out_file)
    plt.close()
    print(f"Bar chart saved to: {out_file}")


if __name__ == "__main__":
    main()
